#----------------EXERCICE 1----------------------
"""
def renverse(mot):
    inverse=""
    for i in range(1,len(mot)+1):
        inverse+=mot[i*-1]
    return inverse
print(renverse("informatique")) #"euqitamrofni"
"""
#----------------EXERCICE 2----------------------
"""
from random import randint
def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0
    while nb_mystere != nb_test and compteur < 11:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
            print("Bravo ! Le nombre était ", nb_mystere)
            print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)
plus_ou_moins()
"""
#----------------EXERCICE 3----------------------
"""
def recherche(caractere,chaine):
    total=0
    for i in range(0,len(chaine)):
        if chaine[i]==caractere:
            total+=1
    return total

print(recherche('e', "sciences")) #2
print(recherche('i', "mississippi")) #4
print(recherche('a', "mississippi"))#0
"""
#----------------EXERCICE 4----------------------
def correspond(mot,mot_a_trous):
    total=0
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(0,len(mot)):
        if mot[i] == mot_a_trous[i] or ("*"):
            total+=1
    if total == len(mot):
        return True
    else:
        return False

print(correspond('INFORMATIQUE','INFO*MA*IQUE')) #True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) #False
print(correspond('STOP', 'S*')) #False
print(correspond('AUTO', '*UT*')) #True