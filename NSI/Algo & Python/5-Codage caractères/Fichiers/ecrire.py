#┍-------------------------------------------------------------┑
#|                         Exo 1.1                             |
#└-------------------------------------------------------------┘
"""
car='a'
print(car)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.2                             |
#└-------------------------------------------------------------┘
"""
car = 'b'
print(ord(car))
print(ord(car)+2)
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.3                             |
#└-------------------------------------------------------------┘
"""
valeur=66
print(chr(valeur))
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.4                             |
#└-------------------------------------------------------------┘
"""
car = 'a'
valeur=ord(car)+2
print(valeur)
print(chr(valeur))
"""
#┍-------------------------------------------------------------┑
#|                         Exo 1.5                             |
#└-------------------------------------------------------------┘
"""
valeur=346
print(chr(valeur))
valeur=0x1f3
print(chr(valeur))
"""
#┍-------------------------------------------------------------┑
#|                           Exo 2                             |
#└-------------------------------------------------------------┘
"""
new_message =""     # initialise new_message avec un message vide
message = input("Veuillez saisir un texte en MAJUSCULE et terminer par ENTER")
print("Vous avez saisi ",message)  # Affiche le message saisi

for n in message:       # pour chaque caractère n dumessage saisi (de la chaine message)
    code_initial = ord(n)       # la variable code_initial prend le code (Unicode)
    code_minuscule = code_initial + 32     # calcul le codecorrespondant au caractère minuscule
    car_minuscule = chr(code_minuscule) # car_minuscule prend le caractère/symbole correspondant
    print(car_minuscule)      # Affiche le caractère obtenu
    new_message = new_message + car_minuscule  # ajoute le caractère obtenu à new_message

print (new_message)    # Affiche le nouveau message
"""
#┍-------------------------------------------------------------┑
#|                           Exo 3                             |
#└-------------------------------------------------------------┘
"""
import os
fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()
"""
#┍-------------------------------------------------------------┑
#|                           Exo 4                             |
#└-------------------------------------------------------------┘
message="Spécialité NSI 2019-2020"

#Ouverture/création du fichier1 en encodage Latin 1
fichier1=open("Exemple_encodage_Latin1.txt",'w',encoding="latin-1")

#Ouverture/création du fichier2 en encodage UTF-8
fichier2=open("Exemple_encodage_UTF-8.txt",'w',encoding="utf-8")

#Ouverture/création du fichier1 en encodage UTF-8 avec signature (BOM)
fichier3=open("Exemple_encodage_UTF-8_BOM.txt",'w',encoding="utf-8-sig")

fichier1.write(message)
fichier2.write(message)
fichier3.write(message)

fichier1.close()
fichier2.close()
fichier3.close()