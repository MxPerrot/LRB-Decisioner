# coding: utf-8 

"""
This script enables the user to compare pokemon and match them against each other.

Author: Maxime Perrot
Date: 2024-12-19
"""


import pandas as pd
import numpy as np
from tqdm import tqdm
from stats_coeff                import get_stats_coeff
from type_effectiveness_coeff   import get_type_effectiveness_coeff
import plotly.express as px
import logging

logger = logging.getLogger(__name__)

###############################################################################
#                                  FUNCTIONS                                  #
###############################################################################


def get_pokemon_by_name(pokemon_df: pd.DataFrame, name: str) -> list | None:
    """
    Get a pokemon from the dataframe by its name

    pokemon_df: pd.DataFrame - the dataframe containing the pokemon data
    name: str - the name of the pokemon

    return: list - the pokemon
    """

    try:
        return pokemon_df[pokemon_df['Name'] == name].iloc[0]
    except IndexError:
        logger.error(f"Pokemon {name} not found in the dataframe")
        return None


def get_team_by_names(pokemon_df: pd.DataFrame, names: list[str]) -> list[list]:
    """
    Get a team of pokemon from the dataframe by their names.

    pokemon_df: pd.DataFrame - the dataframe containing the pokemon data
    names: list[str] - the names of the pokemon

    return: list[list] - the team of pokemon
    """

    return [get_pokemon_by_name(pokemon_df, name) for name in names]


def generate_match_matrix(pokemon_df: pd.DataFrame) -> list[list[float]]:
    """
    Generate a match matrix for all pokemon in the dataframe

    pokemon_df: pd.DataFrame - the dataframe containing the pokemon data

    return: list[list[float]] - the match matrix
    """

    logger.debug('Generating match matrix')

    # # REMOVE OUTLIERS
    # # remove all mega pokemon from df (they have the same # as their non-mega counterpart)
    # pokemon_df = pokemon_df.drop_duplicates(subset=['#'])
    # # remove Shedinja, Happiny and Magikarp
    # pokemon_df = pokemon_df[~pokemon_df['Name'].isin(['Shedinja', 'Happiny', 'Magikarp', 'Feebas', 'Ho-oh'])]

    # generate match matrix        
    pokemon_match_matrix: list = []

    for pokemon in tqdm(pokemon_df.iterrows(), total=len(pokemon_df), colour="green", ncols=80): # for each pokemon
        pokemon_match: list[float] = []
        for opponent in pokemon_df.iterrows(): # for each opponent of said pokemon
            pokemon_match.append( # get the match between the two
                get_match(
                    pokemon[1],
                    opponent[1]
                )
            )
        pokemon_match_matrix.append(pokemon_match)
    
    return pokemon_match_matrix


def display_match_matrix(pokemon_match_matrix: list[list[float]], pokemon_names: list[str]) -> None:
    """
    Display the match matrix as a heatmap and as a dataframe
    
    pokemon_match_matrix: list[list[float]] - the match matrix
    pokemon_names: list[str] - the names of the pokemon, labels for the matrix

    return: None
    """
    logger.debug('Displaying match matrix')

    # turn the matrix into a dataframe
    pmm_df = pd.DataFrame(pokemon_match_matrix)
    
    # print the dataframe
    logger.info(pmm_df)

    # print a description of the dataframe
    logger.info(pmm_df.describe())

    # print the matrix as a heatmap
    fig = px.imshow(
        pokemon_match_matrix,
        labels = dict(x="Pokemon", y="Opponent", color="Win Chance"),
        x = pokemon_names,
        y = pokemon_names,
        text_auto=True
    )
    
    fig.update_xaxes(side="top")
    fig.show()


def get_match(pokemon1: list, pokemon2: list, speed_modifier: float = 0.1) -> float:
    """
    Get the win chance of pokemon1 against pokemon2

    pokemon1: list - the first pokemon
    pokemon2: list - the second pokemon

    return: float - the win chance of pokemon1 against pokemon2
    """
    
    logger.debug(f"Getting the win chance of {pokemon1['Name']} against {pokemon2['Name']}")

    # get stats coeff
    stats_coeff = get_stats_coeff(pokemon1, pokemon2, speed_modifier)

    # get type effectiveness coeff
    type_effectiveness_coeff = get_type_effectiveness_coeff(
        typeAtk1 = pokemon1['Type 1'],
        typeAtk2 = pokemon1['Type 2'],
        typeDef1 = pokemon2['Type 1'],
        typeDef2 = pokemon2['Type 2'])

    win_chance: float = stats_coeff * type_effectiveness_coeff

    logger.debug(f"{pokemon1['Name']} vs {pokemon2['Name']} : {stats_coeff} * {type_effectiveness_coeff} = {win_chance}")

    return win_chance


def get_team_vs_single(team_1: list[list], opponent: list, on_board_modifier: float = 0.2, speed_modifier: float = 0.1) -> list:
    """
    Get the best pokemon from team_1 to fight against opponent
    WARNING: the first pokemon in the team is considered on the board 

    team_1: list[list] - the team of pokemon
    opponent: list - the opponent pokemon

    return: list - the best pokemon from team_1 to fight against opponent
    """

    logger.debug(f"Getting the best pokemon from amongst {[pokemon['Name'] for pokemon in team_1]} to fight against {opponent['Name']}")
    
    max_win_chance: float = 0
    best_pokemon: list = None

    for i, pokemon in enumerate(team_1):
        win_chance = get_match(pokemon, opponent, speed_modifier)
        if i == 0:
            win_chance *= 1 + on_board_modifier
        if win_chance > max_win_chance:
            max_win_chance = win_chance
            best_pokemon = pokemon

    logger.info(f"The best pokemon from the team to fight against {opponent['Name']} is {best_pokemon['Name']}")

    return best_pokemon


def input_team(pokemon_df: pd.DataFrame, query: str = "") -> list[list]:
    """
    Input a team of pokemon from the user, to a maximum of 6 pokemon

    pokemon_df: pd.DataFrame - the dataframe containing the pokemon data

    return: list[list] - the team of pokemon
    """

    team: list = []
    while len(team) < 6:
        name = input(query)
        if name == "":
            if len(team) == 0:
                logger.error("You must have at least one pokemon in your team")
                continue
            else:
                break
        pokemon = get_pokemon_by_name(pokemon_df, name)
        if pokemon is not None:
            team.append(pokemon)
    
    logger.debug(f"Team: {[pokemon['Name'] for pokemon in team]}")
    return team

def input_pokemon(pokemon_df: pd.DataFrame, query: str = "") -> list:
    """
    Input a pokemon from the user

    pokemon_df: pd.DataFrame - the dataframe containing the pokemon data

    return: list - the pokemon
    """

    while True:
        name = input(query)
        if name == "":
            logger.error("You must specify a pokemon")
            continue
        else:
            pokemon = get_pokemon_by_name(pokemon_df, name)
            if pokemon is not None:
                break

    return get_pokemon_by_name(pokemon_df, name)

    
###############################################################################
#                                   PROGRAMS                                  #
###############################################################################
 

def program_match_matrix_all_pokemon(df: pd.DataFrame) -> None:
    """
    Runs the match matrix for all pokemon in the dataframe

    df: pd.DataFrame - the dataframe containing the pokemon data

    return: None
    """

    match_matrix = generate_match_matrix(df)
    display_match_matrix(match_matrix, df['Name'])


def program_match_matrix_with_inputed_team(df: pd.DataFrame) -> None:
    """
    Runs the match matrix with an inputed team of pokemon

    df: pd.DataFrame - the dataframe containing the pokemon data

    return: None
    """

    print(f"\nSpecify a team of pokemon.\nPress Enter to finish.")
    team_1 = input_team(df, "Add a pokemon to your team: ")
    
    match_matrix = generate_match_matrix(pd.DataFrame(team_1))
    display_match_matrix(match_matrix, [pokemon['Name'] for pokemon in team_1])


def program_team_vs_single(df: pd.DataFrame, on_board_modifier: float, speed_modifier: float) -> None:
    """
    Runs the team vs single program

    df: pd.DataFrame - the dataframe containing the pokemon data

    return: None
    """

    print(f"--- Choose the best pokemon to fight against the opponent ---")
    opponent = input_pokemon(df, "\n1. Specify the opponent's pokemon: ")

    print(f"\n2. Specify your team of pokemon.\nIMPORTANT: Enter the pokemon on the board first.\nPress Enter to finish.")
    team_1 = input_team(df, "Add a pokemon to your team: ")
    
    best_pokemon = get_team_vs_single(team_1, opponent, on_board_modifier = on_board_modifier, speed_modifier = speed_modifier)
    print(f"\n3. The best pokemon to fight against {opponent['Name']} is {best_pokemon['Name']} with a win chance of {round(get_match(best_pokemon, opponent, speed_modifier),3)} against {round(get_match(opponent, best_pokemon, speed_modifier),3)}")


def program_single_vs_single(df: pd.DataFrame, speed_modifier: float) -> None:
    """
    Runs the single vs single program

    df: pd.DataFrame - the dataframe containing the pokemon data

    return: None
    """

    print(f"--- Choose the best pokemon to fight against the opponent ---")
    opponent = input_pokemon(df, "\n1. Specify the opponent's pokemon: ")

    your_pokemon = input_pokemon(df, "\n2. Specify your pokemon: ")

    win_chance = get_match(your_pokemon, opponent, speed_modifier)
    opponent_win_chance = get_match(opponent, your_pokemon, speed_modifier)

    print(f"\n3. The win chance of {your_pokemon['Name']} against {opponent['Name']} is {round(win_chance,3)} against {round(opponent_win_chance,3)}")

    if win_chance > opponent_win_chance:
        print(f"\n{your_pokemon['Name']} wins!")
    elif win_chance < opponent_win_chance:
        print(f"\n{opponent['Name']} wins!")

###############################################################################
#                                     MAIN                                    #
###############################################################################


def main(pokemon_data_path: str, delimiter: str, logging_level: str) -> None:
    """
    Main function

    pokemon_data_path: str - the path to the pokemon data
    delimiter: str - the delimiter used in the pokemon data csv file

    return: None
    """

    # CONSTANTS
    ON_BOARD_MODIFIER = 0.2
    SPEED_MODIFIER = 0.1
    TITLE = r"""
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
  _      _____  ____        _____            _     _                           
 | |    |  __ \|  _ \      |  __ \          (_)   (_)                          
 | |    | |__) | |_) |_____| |  | | ___  ___ _ ___ _  ___  _ __   ___ _ __     
 | |    |  _  /|  _ <______| |  | |/ _ \/ __| / __| |/ _ \| '_ \ / _ \ '__|    
 | |____| | \ \| |_) |     | |__| |  __/ (__| \__ \ | (_) | | | |  __/ |       
 |______|_|  \_\____/      |_____/ \___|\___|_|___/_|\___/|_| |_|\___|_|       
               _____             _         _                 _       _             
     /\       |  __ \           | |       (_)               | |     | |            
    /  \      | |  | |_   _  ___| |    ___ _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
   / /\ \     | |  | | | | |/ _ \ |   / __| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
  / ____ \    | |__| | |_| |  __/ |   \__ \ | | | | | | |_| | | (_| | || (_) | |   
 /_/    \_\   |_____/ \__,_|\___|_|   |___/_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                                                                               
By LRB Team       

Example pokemon for testing:
- Charmander
- Bulbasaur
- Squirtle
"""

    # LOGGING
    logging.basicConfig(level=logging_level)
    logger.info('Started')

    # DATA
    df = pd.read_csv(
        pokemon_data_path,
        delimiter = delimiter,
        keep_default_na = False # keep empty string rather than use numpy.nan
    )

    # PROGRAMS
    print(TITLE)
    while True:
        print("\nChoose a program to run:")
        print("  1. Display match matrix for all pokemon (may take a while)")
        print("  2. Display match matrix of a given team")
        print("  3. Predict match team vs single pokemon")
        print("  4. Predict match single pokemon vs single pokemon")
        print("  5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            program_match_matrix_all_pokemon(df)
        elif choice == '2':
            program_match_matrix_with_inputed_team(df)
        elif choice == '3':
            program_team_vs_single(df, ON_BOARD_MODIFIER, SPEED_MODIFIER)
        elif choice == '4':
            program_single_vs_single(df, SPEED_MODIFIER)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    # logger.info('Finished')




if __name__ == '__main__':

    POKEMON_DATA_PATH = 'Pokemon.csv'
    DELIMITER = ','
    main(
        pokemon_data_path   = POKEMON_DATA_PATH,
        delimiter           = DELIMITER,
        logging_level       = logging.ERROR
    )

