import time
import random

N=20000             #longueur du tableau
VALEUR_MAX=25000   #valeur maximale pouvant être contenue dans le tableau

def creationValeursNonTrie(N):  #fonction de génération d'un tableau de valeurs aléatoires
    tableau=[]
    for indice in range(0,N):
        tableau.append(random.randint(1,VALEUR_MAX))
    return tableau

def tri_Selection(tableau):     #fonction de tri par sélection à compléter
    for i in range(0, N - 1):
        indmini = i
        for j in range(i + 1, N):
            if (tableau[j] < tableau[indmini]):
                indmini = j
        if (i != indmini):
            temp = tableau[i]
            tableau[i] = tableau[indmini]
            tableau[indmini] = temp
            #print(tableau[indmini], '<-->', tableau[i], ':', tableau)


tab=creationValeursNonTrie(N)   #génération d'un tableau de valeur aléatoire
print('tableau non trié',tab)
debut = time.time()             #mémorisation de l'heure de début
tri_Selection(tab)
fin = time.time()
print('tableau trié',tab)             #mémorisation de l'heure de fin
print("longueur tableau \t durée de traitement")
print(N,'\t',fin-debut)