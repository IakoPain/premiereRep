#┍-------------------------------------------------------------┑
#|                       Exemple 1                             |
#└-------------------------------------------------------------┘
"""
def afficheTuple(tuple):

    prenom,nom,adresse,codePostal,ville=tuple
    print("prenom",prenom)
    print("nom",nom)
    print("adresse",adresse)
    print("code postal",codePostal)
    print("ville",ville)

tuple=('bruce','wayne','3 impasse de la chauve souris',"72000","le mans")
print(tuple)
"""
#┍-------------------------------------------------------------┑
#|                       Exemple 2                             |
#└-------------------------------------------------------------┘
"""
def calcul(x,coefficientsDroite=tuple):
    a,b=coefficientsDroite
    y=a*x+b
    return(y)
coefficients=(2,1)
print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))
"""
#┍-------------------------------------------------------------┑
#|                       Exemple 3                             |
#└-------------------------------------------------------------┘
"""
from math import sqrt
def distance(ptA,ptB):
    xA,yA=ptA
    xB,yB=ptB
    AB=sqrt((xB-xA)**2+(yB-yA)**2)
    return AB
ptA=(1,1)
ptB=(2,2)
print(distance(ptA,ptB))
"""
#┍-------------------------------------------------------------┑
#|                       Exemple 4                             |
#└-------------------------------------------------------------┘
"""
def rechercheMin(Liste):
    min=Liste[0]
    for indice in range(1,len(Liste)-1):
        if Liste[indice] < min:
            min=Liste[indice]
    return min
lst=[20,8,9,2,35,49]
print(rechercheMin(lst))
"""
#┍-------------------------------------------------------------┑
#|                       Exemple 5                             |
#└-------------------------------------------------------------┘
"""
def rechercheMax(Liste):
    max=Liste[0]
    for indice in range(1,len(Liste)):
        if Liste[indice] > max:
            max=Liste[indice]
    return max
lst=[20,8,9,2,35,49]
print(rechercheMax(lst))
"""
#┍-------------------------------------------------------------┑
#|                       Exemple 6                             |
#└-------------------------------------------------------------┘
"""
def somme(Liste):
    total=0
    for indice in range(1,len(Liste)):
        total=sum(lst)
    return total
lst=[20,8,9,2,35,49]
print(somme(lst))
"""
#┍-------------------------------------------------------------┑
#|                     Exemple 7 & 8                           |
#└-------------------------------------------------------------┘
"""
def moy(Liste):
    total=0
    for indice in range(1,len(Liste)):
        total=sum(lst)
        total=total/indice
    return total
lst=[20,8,9,2,35,49]
print(moy(lst))
"""
#┍-------------------------------------------------------------┑
#|                       Exemple 9                             |
#└-------------------------------------------------------------┘
def rechercheMin(Liste):
    min=Liste[0]
    for indice in range(1,len(Liste)-1):
        if Liste[indice] < min:
            min=Liste[indice]
    return min
lst=[20,8,9,2,35,49]
print(rechercheMin(lst))
def rechercheMax(Liste):
    max=Liste[0]
    for indice in range(1,len(Liste)):
        if Liste[indice] > max:
            max=Liste[indice]
    return max
lst=[20,8,9,2,35,49]
print(rechercheMax(lst))
def moy(Liste):
    total=0
    for indice in range(1,len(Liste)):
        total=sum(lst)
        total=total/indice
    return total
lst=[20,8,9,2,35,49]
print(moy(lst))