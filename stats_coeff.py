def get_stats_coeff(pok1: list, pok2: list) -> float:
    coeffAtk     =   pok1['Attack']  / pok2['Defense']  
    coeffAtkSpe  =   pok1['Sp. Atk'] / pok2['Sp. Def']  
    coeffDef     =   pok1['Defense'] / pok2['Attack']  
    coeffDefSpe  =   pok1['Sp. Def'] / pok2['Sp. Atk'] 
    coeffHP      =   pok1['HP']      / pok2['HP']     

    if(pok1['Speed'] > pok2['Speed']):
        coeffSpeedDef    = 1.2
        coeffSpeedAtk    = 1.1
    elif (pok1['Speed'] < pok2['Speed']):
        coeffSpeedDef    = 0.9
        coeffSpeedAtk    = 0.8
    else:
        coeffSpeedDef    = 1
        coeffSpeedAtk    = 1

    coeffGlob = (
        coeffAtk * coeffAtkSpe * coeffSpeedAtk * coeffDef * coeffDefSpe * coeffSpeedDef * coeffHP  
    )

    return coeffGlob
