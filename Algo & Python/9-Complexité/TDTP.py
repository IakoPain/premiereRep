from pylab import *
EPAISSEUR_FEUILLE=0.0001

def fold(hauteur):
    somme_hauteur=EPAISSEUR_FEUILLE
    pliages=0
    x=[]
    y=[]
    while somme_hauteur<hauteur:
         pliages+=1
         somme_hauteur*=2
         print (somme_hauteur)
         x.append(somme_hauteur)
         y.append(pliages)

    plot(x, y)
    return pliages

print(fold(14))
show()  # affiche la figure à l'écran



