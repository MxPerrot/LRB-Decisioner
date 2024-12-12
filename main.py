# coding: utf-8 


"""

"""


import pandas as pd
import numpy as np
from stats_coeff import get_stats_coeff
from type_effectiveness_coeff import get_type_effectiveness_coeff


def get_match(pokemon1: list, pokemon2: list) -> float:
    # get stats coeff
    stats_coeff = get_stats_coeff(pokemon1, pokemon2)

    # get type effectiveness coeff

    type_effectiveness_coeff = get_type_effectiveness_coeff(
        typeAtk1 = pokemon1['Type 1'],
        typeAtk2 = pokemon1['Type 2'],
        typeDef1 = pokemon2['Type 1'],
        typeDef2 = pokemon2['Type 2'])

    # print(f"{stats_coeff} * {type_effectiveness_coeff}")
    return stats_coeff * type_effectiveness_coeff


def main(pokemon_data_path, delimiter):
    pokemon_match_matrix = []
    df = pd.read_csv(
        pokemon_data_path,
        delimiter = delimiter,
        keep_default_na=False # keep empty string rather than use numpy.nan
    )

    # df['Stat Coeff'] = df.apply(lambda row: statCoeff(row), axis=1)
    get_match(
        df.loc[df['Name'] == 'Charmander'].iloc[0],
        df.loc[df['Name'] == 'Venusaur'].iloc[0]
    )
        
if __name__ == '__main__':

    POKEMON_DATA_PATH = 'Pokemon.csv'
    DELIMITER = ','
    
    main(
        pokemon_data_path = POKEMON_DATA_PATH,
        delimiter = DELIMITER
    )

