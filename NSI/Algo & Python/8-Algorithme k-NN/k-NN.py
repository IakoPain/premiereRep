#┍-------------------------------------------------------------┑
#|                         Exemple 1                           |
#└-------------------------------------------------------------┘
"""
def distance(x1,x2):
    return abs(x1-x2)

def Kvoisins(L,k,x):
    listeDistanceIndice=[]
    for i in range(len(L)):
        d= distance(x,L[i])
        listeDistanceIndice.append([d,i])
    listeDistanceIndice.sort()
    voisins=[]
    for i in range(k):
       voisins.append(listeDistanceIndice[i][1])
    return voisins
L=[0,1,2,4,6,7,8]
classes=['T','C','C','T','T','C','C']
x=3
k=3

print('liste des indices',Kvoisins(L,k,x))
"""
#┍-------------------------------------------------------------┑
#|                         Exemple 2                           |
#└-------------------------------------------------------------┘
"""
def distance(x1,x2):
    return abs(x1-x2)

def Kvoisins(L,k,x):
    listeDistanceIndice=[]
    for i in range(len(L)):
        d= distance(x,L[i])
        listeDistanceIndice.append([d,i])
    listeDistanceIndice.sort()
    voisins=[]
    for i in range(k):
       voisins.append(listeDistanceIndice[i][1])
    return voisins
def predireClasse(L,classes,k,x):
    voisins=Kvoisins(L,k,x)
    classespossibles = ['C','T']
    decompte=[0,0]
    for v in voisins:
        if classes[v]=='C':
            decompte[0] +=1
        else:
            decompte[1] +=1
    if decompte[1]>decompte[0]:
        classeChoisie=classespossibles[1]
    else:
        classeChoisie=classespossibles[0]
    return  classeChoisie
L=[0,1,2,4,6,7,8]
classes=['T','C','C','T','T','C','C']
x=3
k=3
print('classe du nouvel element',predireClasse(L,classes,k,x))
"""
#┍-------------------------------------------------------------┑
#|                         Exemple 2                           |
#└-------------------------------------------------------------┘
def distance(x1,x2):
    return abs(x1-x2)

def Kvoisins(L,k,x):
    listeDistanceIndice=[]
    for i in range(len(L)):
        d= distance(x,L[i])
        listeDistanceIndice.append([d,i])
    listeDistanceIndice.sort()
    voisins=[]
    for i in range(k):
       voisins.append(listeDistanceIndice[i][1])
    return voisins
def predireClasse(L,classes,k,x):
    voisins=Kvoisins(L,k,x)
    classespossibles = ['C','T',"R"]
    decompte=[0,0,0]
    for v in voisins:
        if classes[v]=='C':
            decompte[0] +=1
        elif classes[v]=='T':
            decompte[1] +=1
        else:
            decompte[2] +=1
    if decompte[1]>decompte[0] and decompte[1]>decompte[2]:
        classeChoisie=classespossibles[1]
    elif decompte[0]>decompte[1] and decompte[0]>decompte[2]:
        classeChoisie=classespossibles[0]
    else:
        classeChoisie=classespossibles[2]
    return  classeChoisie
L=[0,1,2,4,6,7,8]
classes=['R','T','C','C','C','R','R','R']
x=8
k=3
print('classe du nouvel element',predireClasse(L,classes,k,x))