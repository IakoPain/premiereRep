"""
tp3 recherche dichotomique
"""
import time
import random

N=1000           #longueur du tableau
VALEUR_MAX=100   #valeur maximale pouvant être contenue dans le tableau

def creationValeurs(N):
    tableau=[]
    for indice in range(0,N):
        valeur=random.randint(1,VALEUR_MAX)
        while valeur in tableau:
            valeur = random.randint(1, VALEUR_MAX)
        tableau.append(valeur)
    return sorted(tableau)


def recherche_dichotomique( element, tableau ):
    bas = 0
    haut = len(tableau)-1
    trouve=False
    #print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format('bas:','haut:','milieu:','valeur:','bas<=haut:','trouve:'))
    while bas <= haut and trouve==False:
        milieu = (bas + haut) // 2
        if element==tableau[milieu]:
            trouve=True
            #print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format(bas, haut, milieu, tableau[milieu], bas <= haut, trouve))
        else:
            #print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format(bas, haut, milieu, tableau[milieu], bas <= haut, trouve))
            if element>tableau[milieu]:
                bas = milieu+1
            else :
                haut = milieu-1
        time.sleep(0.1)
    #print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format(bas, haut, milieu, tableau[milieu], bas <= haut, trouve))
    if trouve==True:
        indice = milieu
    else:
        indice = -1
    return indice


def affichage(tableau):
    print('valeur',end='')
    for x in range(0, len(tableau)):
        print('{0:4d}'.format(tableau[x]),end='')
    print()
    print('indice', end='')
    for x in range(0, len(tableau)):
        print('{0:4d}'.format(x),end='')
    print()

tableau=creationValeurs(N)
affichage(tableau)
#tableau=[10,12,15,21,25,31,35,37,42,44,49,53,61,72,75,85]
#print (tableau)


chiffreAtrouver=tableau[1]
print('chiffre à trouver',chiffreAtrouver)

debut = time.time()
indice=recherche_dichotomique(chiffreAtrouver,tableau)
fin = time.time()
print("la valeur",tableau[indice],"se trouve à l'indice", indice,"dans le tableau:")
print(N,'\t',fin-debut)




