# coding: utf-8 

"""
This script defines the functions to get type effectiveness coefficient of the attack types against the defense types of two pokemons

Author: Ewan Lansonneur
Date: 2024-12-19
"""

import json

with open('type_chart.json') as f:
    type_effectiveness = json.load(f)

def get_type_effectiveness_coeff(typeAtk1: str, typeAtk2: str, typeDef1: str, typeDef2: str, show=False) -> float: 
    """
    Get the type effectiveness coefficient of the attack types against the defense types
    
    typeAtk1: str - the first attack type
    typeAtk2: str - the second attack type
    typeDef1: str - the first defense type
    typeDef2: str - the second defense type
    
    return: float - the type effectiveness coefficient of the attack types against the defense types
    """

    coeff = type_effectiveness[typeAtk1][typeDef1] 

    if typeAtk2 != "":

        coeff = coeff * type_effectiveness[typeAtk2][typeDef1]     
        if typeDef2 != "":         
            coeff = coeff * type_effectiveness[typeAtk1][typeDef2]         
            coeff = coeff * type_effectiveness[typeAtk2][typeDef2] 
    else:     
        if typeDef2 != "":         
            coeff = coeff * type_effectiveness[typeAtk1][typeDef2] 

    return coeff