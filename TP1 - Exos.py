#------------------
#Exo 1
"""
a=4
carre=a**2
print("La valeur de 'a' est",a,"au carré est de",carre)
"""
#------------------
#Exo 2
"""
kilometre=100
miles=kilometre/1.609
print("La distance de",kilometre,"kilomètre est de",miles,"en miles")
"""
#------------------
#Exo 3
"""
a=2
b=3
print("Avant échange a=",a," et b=",b)
temp=a
a=b
b=temp
print("Après échange a=",a," et b=",b)
"""
#------------------
#Exo 4
"""
valeur_tva=20
prix_ht=40
tva=prix_ht*valeur_tva/100
prix_ttc=prix_ht+tva
print("Prix HT du produit",prix_ht," €")
print("Indice de la TVA en 2015",tva," €")
print("Valeur de la TVA",tva," €")
print("Prix TTC: ",prix_ttc," €")
"""
#------------------
#Exo 5
"""
a=3
b=-15
r=a+b
if (r<0):
    print("Le produit est négatif")
else:
    print("Le produit est positif")
"""
#------------------
#Exo 6
"""
age=14
if (age>=6) and (age<=7):
    print("Poussin")
elif (age>=8) and (age<=9):
    print("Pupille")
elif (age>=10) and (age<=11):
    print("Minime")
elif (age>=12) and (age<=15):
    print("Cadet")
elif (age>=16) and (age<=255):
    print("Hors catégorie")
"""
#------------------
#Exo 7
"""
nb_valeur=10
result=0
temp=0
for i in range(0,nb_valeur+1):
    result=result+temp
    temp=temp+1
print(result)
"""
#------------------
#Exo 8
"""
for a in range(11):
    for i in range(11):
        print(a*i,end="\t")
    print()
"""