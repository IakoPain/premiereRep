# Création de fichiers texte à partir de Python3
# avec l'utilisation de différentes directives d'encodage

message="Spécialité NSI 2019-2020"

#Ouverture/création du fichier 1 en encodage Latin 1
fichier1=open("Exemple_encodage_Latin1.txt",'w',encoding="latin-1")

#Ouverture/création du fichier 1 en encodage UTF-8
fichier2=open("Exemple_encodage_UTF-8.txt",'w',encoding="utf-8")

#Ouverture/création du fichier 1 en encodage UTF-8 avec signature (BOM)
fichier3=open("Exemple_encodage_UTF-8_BOM.txt",'w',encoding="utf-8-sig")

fichier1.write(message)
fichier2.write(message)
fichier3.write(message)

fichier1.close()
fichier2.close()
fichier3.close()

