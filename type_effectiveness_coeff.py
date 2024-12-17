import pandas as pd
import numpy as np
import math
import json

with open('type_chart.json') as f:
    type_effectiveness = json.load(f)

def get_type_effectiveness_coeff(typeAtk1: str, typeAtk2: str, typeDef1: str, typeDef2: str, show=False) -> float: 

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