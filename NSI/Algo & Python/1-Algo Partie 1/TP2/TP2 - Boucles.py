#┍-------------------------------------------------------------┑
#|                          Exo 1                              |
#└-------------------------------------------------------------┘
"""
for n in range (1-1,15+1):
    print (n)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 2                              |
#└-------------------------------------------------------------┘
"""
for n in range (-15,0+1):
    print (n)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 3                              |
#└-------------------------------------------------------------┘
"""
n=int(input("Votre valeur de début : "))
m=int(input("Votre valeur de fin : "))
for g in range (n,m+1):
    print(g)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 4                              |
#└-------------------------------------------------------------┘
"""
n=int(input("Votre valeur de début : "))
for g in range (n,n+11):
    print(g)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 5                              |
#└-------------------------------------------------------------┘
"""
p=0
n=int(input("Quelle table de multiplication voulez vous ?"))
j=n
for i in range (1,12):
    n=n*p
    print(n)
    p=p+1
    n=j
"""
#┍-------------------------------------------------------------┑
#|                          Exo 6                              |
#└-------------------------------------------------------------┘
"""
max=0
for n in range(5):
    nb=int(input("Saisir un nombre "))
    if nb>max:
        max=nb
print ("Le nombre le plus grand est", max)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 7                              |
#└-------------------------------------------------------------┘
"""
valeur=0
max=0
portee=int(input("Saisir le nombre de valeur a entrer :"))
while portee>0:
    nb=int(input("Saisir un nombre "))
    if nb>max:
        max=nb
    portee=portee-1
print ("Le nombre le plus grand est", max)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 8                              |
#└-------------------------------------------------------------┘
"""
valeur=0
somme=0
while valeur >=0:
    valeur=int(input("Saisir un nombre"))
    somme=somme+valeur
print(somme)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 9                              |
#└-------------------------------------------------------------┘
"""
menu=0
q=-1
while menu!=q:
    print("1 : Charger le fichier")
    print("2 : Sauvegarder le fichier")
    print("3 : Afficher les données")
    print("4 : Modifier les données")
    print("q : Quitter")
    menu=input("Votre choix ?")
    if menu == "1":
        print("Chargement")
    elif menu == "2":
        print("Sauvegarde")
    elif menu == "3":
        print("Affichage")
    elif menu == "4":
        print("Modification")
    elif menu == "q":
        print("Au revoir")
        menu=-1
    else:
        print("Erreur")
        menu=-1
"""
#┍-------------------------------------------------------------┑
#|                         Exo 10                              |
#└-------------------------------------------------------------┘
"""
from random import *
valeur=0
nombre = randint(1,20)
valeur=int(input("Votre Nombre "))
while valeur > nombre or valeur < nombre:
    if valeur > nombre:
        print("Nombre trop grand")
        valeur=int(input("Votre Nombre "))
    elif valeur < nombre:
        print("Nombre trop petit")
        valeur=int(input("Votre Nombre "))
print("Exact")
"""
#┍-------------------------------------------------------------┑
#|                         Exo 11                              |
#└-------------------------------------------------------------┘
"""
from random import *
valeur=0
coups=0
nombre = randint(1,20)
valeur=int(input("Votre Nombre "))
while valeur > nombre or valeur < nombre:
    if valeur > nombre:
        print("Nombre trop grand")
        coups=coups+1
        valeur=int(input("Votre Nombre "))
    elif valeur < nombre:
        print("Nombre trop petit")
        coups=coups+1
        valeur=int(input("Votre Nombre "))
print("Exact , votre nombre de coups est de",coups+1,"coups")
"""
#┍-------------------------------------------------------------┑
#|                         Exo 12                              |
#└-------------------------------------------------------------┘
"""
k=3
from random import *
while k!=1:
    k=3
    valeur=0
    coups=0
    nombre = randint(1,20)
    valeur=int(input("Votre Nombre "))
    while valeur > nombre or valeur < nombre:
        if valeur > nombre:
            print("Nombre trop grand")
            coups=coups+1
            valeur=int(input("Votre Nombre "))
        elif valeur < nombre:
            print("Nombre trop petit")
            coups=coups+1
            valeur=int(input("Votre Nombre "))
    print("Exact , votre nombre de coups est de",coups+1,"coups")
    while k==3:
        temp=input("Rejouer ? (O=Oui ; N=Non) ")
        if temp == "N":
            k=1
        elif temp == "O":
            k=0
        else:
            k=3
"""
#┍-------------------------------------------------------------┑
#|                         Exo 13                              |
#└-------------------------------------------------------------┘
"""
from math import *
xA=int(input("Abscisse du point A ? "))
yA=int(input("Ordonnée du point A ? "))
xB=int(input("Abscisse du point B ? "))
yB=int(input("Ordonnée du point B ? "))
AB=sqrt(xB-xA)**2+(yB-yA)**2
print(AB)
"""