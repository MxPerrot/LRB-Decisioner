import pandas as pd

def statCoeff(pok1, pok2):
    coefAtt= (pok1['Attack']/pok2['Defense'])
    coefAttSpe= (pok1['Sp. Atk']/pok2['Sp. Def'])
    coefDef= (pok1['Defense']/pok2['Attack'])
    coefDefSpe= (pok1['Sp. Def']/pok2['Sp. Atk'])
    coefHP= (pok1['HP']/pok2['HP'])
    coefGlob=(coefAtt+coefAttSpe+coefDef+coefDefSpe+coefHP)/5

    if(pok1['Speed']>pok2['Speed']):
        coefSpeed=1.1
    elif(pok1['Speed']<pok2['Speed']):
        coefSpeed=0.9
    else:
        coefSpeed=1

    coefGlob=coefGlob*coefSpeed

    return coefGlob


df = pd.read_csv('Pokemon.csv')


print(statCoeff(df.iloc[4],df.iloc[0]))
