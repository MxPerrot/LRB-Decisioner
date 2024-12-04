def statCoeff(pok1, pok2):
    coefAtt= (pok1['Attack']-pok2['Defense'])/100
    coefAttSpe= (pok1['Sp. Atk']-pok2['Sp. Def'])/100
    coefDef= (pok1['Defense']-pok2['Attack'])/100
    coefDefSpe= (pok1['Sp. Def']-pok2['Sp. Atk'])/100
    coefHP= (pok1['HP']-pok2['HP'])/100
    coefGlob=(coefAtt+coefAttSpe+coefDef+coefDefSpe+coefHP)/5

    coefSpeed= (pok1['Speed']-pok2['Speed'])/100
    if(coefSpeed>0):
        coefSpeed=1.2
    else if (coefSPeed<0):
        coefSpeed=0.8
    else:
        coefSpeed=1

    coefGlob=coefGlob*coefSpeed

    return coefGlob
