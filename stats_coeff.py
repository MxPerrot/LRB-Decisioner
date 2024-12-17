# coding: utf-8 

"""
This script defines the functions to get the stats coefficient of two pokemons

Author: Damien Goupil
Date: 2024-12-19
"""

def get_stats_coeff(pok1: list, pok2: list, speed_modifier: float = 0.1) -> float:
    """
    Get the stats coefficient of the first pokemon against the second pokemon

    pok1: list - the first pokemon
    pok2: list - the second pokemon

    return: float - the stats coefficient of the first pokemon against the second pokemon
    """
    
    coeffAtk     =   pok1['Attack']  / pok2['Defense']  
    coeffAtkSpe  =   pok1['Sp. Atk'] / pok2['Sp. Def']  
    coeffDef     =   pok1['Defense'] / pok2['Attack']  
    coeffDefSpe  =   pok1['Sp. Def'] / pok2['Sp. Atk'] 
    coeffHP      =   pok1['HP']      / pok2['HP']     

    if(pok1['Speed'] > pok2['Speed']):
        coeffSpeedDef    = 1 + 2 * speed_modifier
        coeffSpeedAtk    = 1 + speed_modifier
    elif (pok1['Speed'] < pok2['Speed']):
        coeffSpeedDef    = 1 - speed_modifier
        coeffSpeedAtk    = 1 - 2 * speed_modifier
    else:
        coeffSpeedDef    = 1
        coeffSpeedAtk    = 1

    coeffGlob = (
        coeffAtk * coeffAtkSpe * coeffSpeedAtk * coeffDef * coeffDefSpe * coeffSpeedDef * coeffHP  
    )

    return coeffGlob
