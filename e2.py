"""
Ion Zarija, José Villalba
22/01/2024
ASIXc1A M03 UF1 A5 pr5
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
listRandom=[]
listPar=[]
listSenar=[]
totPar=0
totSen=0
import random

for x in range(100):
    listRandom.append((random.randint(1,50)))
    if x % 2 == 0:
        listPar.append(listRandom[x])
        totPar += listRandom[x]
    else:
        listSenar.append(listRandom[x])
        totSen += listRandom[x]
print("La mitjana dels nombres parells són :", totPar/len(listPar))
print("La mitjana dels nombres senars són :", totSen/len(listSenar))
