# coding: utf-8 


"""

"""


import pandas as pd

def main(pokemon_data_path, delimiter, index_col_name):
    df = pd.read_csv(
        pokemon_data_path,
        delimiter = delimiter,
        index_col = index_col_name
    )

    print(df.head())


if __name__ == '__main__':

    POKEMON_DATA_PATH = 'Pokemon.csv'
    DELIMITER = ','
    INDEX_COL_NAME = '#'
    
    main(
        pokemon_data_path = POKEMON_DATA_PATH,
        delimiter = DELIMITER,
        index_col_name = INDEX_COL_NAME
    )
