#┍-------------------------------------------------------------┑
#|                         Exo 1.1                             |
#└-------------------------------------------------------------┘
"""
stock={'poires':5,'pommes':10,'fraises':35}
print(len(stock))
print(stock['fraises'])
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.2                             |
#└-------------------------------------------------------------┘
"""
stock={'poires':5,'pommes':10,'fraises':35}
inventaire=""
for nom in stock.keys():
    inventaire += nom + ', '
print(inventaire)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.3                             |
#└-------------------------------------------------------------┘
"""
stock={'poires':5,'pommes':10,'fraises':35}
for num in stock.values():
    print (num)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.4                             |
#└-------------------------------------------------------------┘
"""
stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

for nom, num in stock.items():
    print(nom, '->',num)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.5                             |
#└-------------------------------------------------------------┘
"""
stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print('fraises' in stock.keys())
print('banane' in stock.keys())
print(7 in stock.values())
print(5 in stock.values())
print(3 in stock.values())
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.6                             |
#└-------------------------------------------------------------┘
"""
stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
stock["fraises"]=20
print(stock)
stock["abricots"]=15
print(stock)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.7                             |
#└-------------------------------------------------------------┘
"""
stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
del stock["fraises"]
print(stock)
valeur = stock.pop("pommes")
print(stock)
print(valeur)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 2.1                             |
#└-------------------------------------------------------------┘
"""
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
d['prenom']='Jacques'
"""
#┍-------------------------------------------------------------┑
#|                         Exo 2.2                             |
#└-------------------------------------------------------------┘
"""
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
print(d.keys())
"""
#┍-------------------------------------------------------------┑
#|                         Exo 2.3                             |
#└-------------------------------------------------------------┘
"""
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
print(d.values())
"""
#┍-------------------------------------------------------------┑
#|                         Exo 2.4                             |
#└-------------------------------------------------------------┘
"""
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
print(d.items())
"""
#┍-------------------------------------------------------------┑
#|                         Exo 2.5                             |
#└-------------------------------------------------------------┘
"""
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
print(d['prenom'], d['nom'], "a", d['age'], "ans")
"""
#┍-------------------------------------------------------------┑
#|                          Exo 3                              |
#└-------------------------------------------------------------┘
"""
D={'Croissant':6,'Pizza':2,'Café en grains (sachet de 500gr)':3,'Riz (sachet de 1kg)':1}
print(D)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 4                              |
#└-------------------------------------------------------------┘
"""
D={'Croissant':6,'Pizza':2,'Café en grains (sachet de 500gr)':3,'Riz (sachet de 1kg)':1}
D['Pizza'] += 1
print(D)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 5                              |
#└-------------------------------------------------------------┘
"""
D={'Croissant':6,'Pizza':2,'Café en grains (sachet de 500gr)':3,'Riz (sachet de 1kg)':1}
for nom, num in D.items():
    print(nom, '->',num)
"""
#┍-------------------------------------------------------------┑
#|                          Exo 6                              |
#└-------------------------------------------------------------┘
"""
def occurrences(chaine) :
   D = {}
   for charactère in chaine :
      if charactère in D.keys():
        D[charactère]+=1
      else:
        D[charactère]=1
   return D
print(occurrences('tortue'))
"""
#┍-------------------------------------------------------------┑
#|                          Exo 7                              |
#└-------------------------------------------------------------┘
"""
def anagramme(chaine1 , chaine2):
    occurenceChaine1 = occurence(chaine1)
    occurenceChaine2 = occurence(chaine2)
    return occurenceChaine1 == occurenceChaine2
    print(anagramme('tortue', 'tourne' ))
    print(anagramme('imaginer', 'migraine' ))
"""
#┍-------------------------------------------------------------┑
#|                          Exo 8                              |
#└-------------------------------------------------------------┘
"""
def anagramme(chaine1 , chaine2):
    occurenceChaine1 = occurence(chaine1)
    occurenceChaine2 = occurence(chaine2)
    return occurenceChaine1 == occurenceChaine2
    print(anagramme('le rechauffement climatique', 'ce fuel qui tache le firmament' ))
"""
#┍-------------------------------------------------------------┑
#|                         Exo 9.5                             |
#└-------------------------------------------------------------┘
"""
def anagramme(chaine1 , chaine2):
    occurenceChaine1 = occurence(chaine1)
    occurenceChaine2 = occurence(chaine2)
    del occurence(chaine1) =" "
    del occurence(chaine2) =" "
    return occurenceChaine1 == occurenceChaine2
print(anagramme('tortue', 'tourne' ))
print(anagramme('imaginer', 'migraine' ))
"""
#┍-------------------------------------------------------------┑
#|                         Exo 10                              |
#└-------------------------------------------------------------┘
"""
def renduMonnaie(somme,pieces):
    choisies={}
    for p in pieces:
        choisies[p]=0
        while somme>=p:
            somme=somme-p
            choisies[p]=choisies[p]+1
    return choisies

pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
#┍-------------------------------------------------------------┑
#|                         Exo 10B                             |
#└-------------------------------------------------------------┘
"""
def renduMonnaie(somme,pieces):
   choisies = {}
   for p in pieces:
      nb=somme//p
      choisies[p]=nb
      somme=somme-nb*p
   return choisies

pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
#┍-------------------------------------------------------------┑
#|                         Exo 12                              |
#└-------------------------------------------------------------┘
"""
import csv
fichier = open("donnees.csv", "r")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_personnes = []
for ligne in lecture_fichier:
    liste_personnes.append(dict(ligne))
fichier.close()

for personne in liste_personnes :
    print(personne)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 13B                             |
#└-------------------------------------------------------------┘
"""
import csv
fichier = open("Ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnees = []
for ligne in lecture_fichier:
    liste_donnees.append(dict(ligne))
fichier.close()

print(liste_donnees)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 14                              |
#└-------------------------------------------------------------┘
"""
import csv
fichier = open("Ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnees = []
for ligne in lecture_fichier:
    liste_donnees.append(dict(ligne))
fichier.close()

for donnees in liste_donnees:
    print("Altitude =" , donnees['Altitude m'], "mètres")
    print("Durée de vol =" , donnees['Durée'])
"""
#┍-------------------------------------------------------------┑
#|                         Exo 15                              |
#└-------------------------------------------------------------┘
"""
import csv
fichier = open("Ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnees = []
for ligne in lecture_fichier:
    liste_donnees.append(dict(ligne))
fichier.close()

for donnees in liste_donnees:
    print(((float(donnees['Temp Int C'])) + (float(donnees['Temp Ext C'])))/2)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 16                              |
#└-------------------------------------------------------------┘
"""
import csv
fichier = open("Ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_enregistrements = []
for ligne in lecture_fichier:
    liste_enregistrements.append(dict(ligne))
fichier.close()

horaire_tmp_min = ''
tmp_min = 100.0
for enregistrement in liste_enregistrements:
    if float(enregistrement['Temp Ext C']) < tmp_min :
        tmp_min = float(enregistrement['Temp Ext C'])
        horaire_tmp_min = enregistrement['Horaire']
print(horaire_tmp_min,tmp_min)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 17A                             |
#└-------------------------------------------------------------┘
"""
from pylab import *

x = [1, 3, 4, 6]
y = [2, 3, 5, 1]
plot(x, y) # affiche y en fonction de x

show() # affiche la figure l’écran
"""
