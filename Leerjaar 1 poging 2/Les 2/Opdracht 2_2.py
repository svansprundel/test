cijferICOR = 8
cijferCSN = 6.5
cijferPROGG = 7

Totaal = cijferCSN + cijferCSN + cijferPROGG
Gemiddelde = round(Totaal / 3,1)
Beloning = cijferPROGG * 30 + cijferCSN * 30 + cijferICOR *30
Overzicht = 'Mijn cijfer (gemiddeld een ' + str(Gemiddelde) + ' )leveren een beloning van '+ str(Beloning) + ' op!'
print(Overzicht)
