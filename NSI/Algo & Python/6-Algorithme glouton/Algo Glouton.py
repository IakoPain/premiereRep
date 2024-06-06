#┍-------------------------------------------------------------┑
#|                          Test 1                             |
#└-------------------------------------------------------------┘
"""
def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies


#pieces en centimes d'euros
pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
#┍-------------------------------------------------------------┑
#|                          Test 2                             |
#└-------------------------------------------------------------┘
"""
def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies

pieces=[4,3,1]
somme=6
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
#┍-------------------------------------------------------------┑
#|                          Test 3                             |
#└-------------------------------------------------------------┘
"""
def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies

#pieces en euros
pieces=[10,5,2]
somme=31
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
#┍-------------------------------------------------------------┑
#|                           Test                              |
#└-------------------------------------------------------------┘
"""
def remplirSac(objets,poidsMax):
    p=0
    n=len(objets)
    objetsChoisis=[0]*n
    for i in range(0,n):
        if p+objets[i][1]<=poidsMax:
            objetsChoisis[i]=1
            p = p + objets[i][1]
    return objetsChoisis

#liste du matériel
objets=[[2,1],[5,0.5],[1,0.2],[3,4]]
objets=list(reversed(sorted(objets)))
print(objets)
poidsMax=4.7
print('Les objets choisis sont')
print(remplirSac(objets,poidsMax))
"""
#┍-------------------------------------------------------------┑
#|                        Exercice 1                           |
#└-------------------------------------------------------------┘
"""
def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies

pieces=[50,20,10,5,2,1]
somme=99
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
#┍-------------------------------------------------------------┑
#|                        Exercice 2                           |
#└-------------------------------------------------------------┘
"""
#liste du matériel
def remplirSac(objets,poidsMax):
    p=0
    n=len(objets)
    objetsChoisis=[0]*n
    for i in range(0,n):
        if p+objets[i][1]<=poidsMax:
            objetsChoisis[i]=1
            p = p + objets[i][1]
    return objetsChoisis

objets=[[6,5.0,'chaussures'],[5,5.0,'habits'],[4.5,2.0,'trousse de toilette'],[4,2.0,'crèmes'],[3,8.0,'livres'],[2,2.0,'palmes tuba'],[1,0.5,'guide touristique']]
poidsMax=23
print('Les objets choisis sont')
objetsChoisis=remplirSac(objets,poidsMax)
for n in range(len(objetsChoisis)):
    if objetsChoisis[n]==1:
        print(objets[n][2])
"""
#┍-------------------------------------------------------------┑
#|                        Exercice 3                           |
#└-------------------------------------------------------------┘
def remplirCamion(meubles,volumeMax):
    v=0
    n=len(meubles)
    meublesChoisis=[]
    for i in range(0,n):
        meublesChoisis.append(meubles[i][0])
        v+=meubles[i][1]
    return meublesChoisis


#liste des objets
meubles=[['armoire',3],['fauteuil',1.1],['lave vaisselle',1.0],['lit',0.9],['ordinateur',0.2]]
print(meubles)
volumeMax=5
print('Les meubles choisis sont')
meublesChoisis=remplirCamion(meubles,volumeMax)
print(meublesChoisis)
