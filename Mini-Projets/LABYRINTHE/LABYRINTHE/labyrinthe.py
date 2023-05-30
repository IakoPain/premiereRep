"""
Programme réalisé par nom, prénom, classe
"""
import pygame
import csv
import time


#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 326))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
NOIR=(0,0,0)
BLEU=(0,0,255)
ROUGE=(255,0,0)
VERT=(0,255,0)
BLANC=(255,255,255)
CARRE=7
win=0
f = open("map.csv", "r")

if win == 0:
    f = open("map.csv", "r")
elif win ==1:
    f = open("map2.csv", "r")
c = csv.reader(f, delimiter=',')
tableau = []
for ligne in c:
    tableau.append(ligne)
f.close()
#for l in tableau:
#    print(l)

print(len(tableau),len(tableau[0]))


d=2 #0 nord, 1 est ,2 sud,3 ouest
x=1 #depart
y=7

startTempo=0

img0=pygame.image.load("img_dungeon/0.gif")
img0_1=pygame.image.load("img_dungeon/0-1.gif")
img0_2=pygame.image.load("img_dungeon/0-2.gif")
img0_3=pygame.image.load("img_dungeon/0-3.gif")
img1_1=pygame.image.load("img_dungeon/1-1.gif")
img1_2=pygame.image.load("img_dungeon/1-2.gif")
img1_3=pygame.image.load("img_dungeon/1-3.gif")
img2_1=pygame.image.load("img_dungeon/2-1.gif")
img2_2=pygame.image.load("img_dungeon/2-2.gif")
img2_3=pygame.image.load("img_dungeon/2-3.gif")
img3_1=pygame.image.load("img_dungeon/3-1.gif")
img3_2=pygame.image.load("img_dungeon/3-2.gif")
img4_1=pygame.image.load("img_dungeon/4-1.gif")


#background 4
def b01():
    fenetre.blit(img0_1,(0,60))

def b02():
    fenetre.blit(img0_2,(278,60))

def b03():
    fenetre.blit(img0_3,(149,60))

#background 3
def b11():
    fenetre.blit(img1_1,(0,49))

def b12():
    fenetre.blit(img1_2,(298,49))

def b13():
    fenetre.blit(img1_3,(120,49))

#background 2
def b21():
    fenetre.blit(img2_1,(0,22))

def b22():
    fenetre.blit(img2_2,(328,22))

def b23():
    fenetre.blit(img2_3,(64,22))

#background 1
def b31():
    fenetre.blit(img3_1,(0,0))

def b32():
    fenetre.blit(img3_2,(384,0))



def base():
#affiche du fond du labyrinthe
    fenetre.blit(img0,(0,0))  #afficher l'image à la prochaine actualisation
    afficheCarte(450,0)

def afficheMurNord():
#background 0
    global x,y
    base()
    if y>2:
        if tableau[y-3][x-1] == '0':    # on cherche dans le tableau si la valeur( y-3, x-1) est 0 ALORS on affiche b01()
            b01()                     #  cela correspond à afficher le mur de gauche et qu'il y a 3 cases en face du joueur
        if tableau[y-3][x+1] == '0':
            b02()                    # cela correspond à afficher le mur de droite et qu'il y a 3 cases en face du joueur
        if tableau[y-3][x] == '0':
            b03()                   # cela correspond à afficher le mur au centre et qu'il y a 3 cases en face du joueur
    #background 1
    if y>1:
        if tableau[y-2][x-1] == '0': # idem 2 cases devant le joueur
            b11()
        if tableau[y-2][x+1] == '0':
            b12()
        if tableau[y-2][x] == '0':
            b13()
    #background 2
    if tableau[y-1][x-1] == '0':  # idem 1 case devant le joueur
        b21()
    if tableau[y-1][x+1] == '0':
        b22()
    if tableau[y-1][x] == '0':
        b23()
    #background 3
    if tableau[y][x-1] == '0': # idem mais de chaque coté du joueur
        b31()
    if tableau[y][x+1] == '0':
        b32()

def afficheMurSud():
#background 0
    global x,y
    base()
    if y<len(tableau)-3:
        if tableau[y+3][x+1] == '0':    # on cherche dans le tableau si la valeur( y-3, x-1) est 0 ALORS on affiche b01()
            b01()                     #  cela correspond à afficher le mur de gauche et qu'il y a 3 cases en face du joueur
        if tableau[y+3][x-1] == '0':
            b02()                    # cela correspond à afficher le mur de droite et qu'il y a 3 cases en face du joueur
        if tableau[y+3][x] == '0':
            b03()                   # cela correspond à afficher le mur au centre et qu'il y a 3 cases en face du joueur
    #background 1
    if y<len(tableau)-2:
        if tableau[y+2][x+1] == '0': # idem 2 cases devant le joueur
            b11()
        if tableau[y+2][x-1] == '0':
            b12()
        if tableau[y+2][x] == '0':
            b13()
    #background 2
    if tableau[y+1][x+1] == '0':  # idem 1 case devant le joueur
        b21()
    if tableau[y+1][x-1] == '0':
        b22()
    if tableau[y+1][x] == '0':
        b23()
    #background 3
    if tableau[y][x+1] == '0': # idem mais de chaque coté du joueur
        b31()
    if tableau[y][x-1] == '0':
        b32()

def afficheMurEst():
#background 0
    global x,y
    base()
    if x<len(tableau[0])-3:
        if tableau[y-1][x+3] == '0':    # on cherche dans le tableau si la valeur( y-3, x-1) est 0 ALORS on affiche b01()
            b01()                     #  cela correspond à afficher le mur de gauche et qu'il y a 3 cases en face du joueur
        if tableau[y+1][x+3] == '0':
            b02()                    # cela correspond à afficher le mur de droite et qu'il y a 3 cases en face du joueur
        if tableau[y][x+3] == '0':
            b03()                   # cela correspond à afficher le mur au centre et qu'il y a 3 cases en face du joueur
    #background 1
    if x<len(tableau[0])-2:
        if tableau[y-1][x+2] == '0': # idem 2 cases devant le joueur
            b11()
        if tableau[y+1][x+2] == '0':
            b12()
        if tableau[y][x+2] == '0':
            b13()
    #background 2
    if tableau[y-1][x+1] == '0':  # idem 1 case devant le joueur
        b21()
    if tableau[y+1][x+1] == '0':
        b22()
    if tableau[y][x+1] == '0':
        b23()
    #background 3
    if tableau[y-1][x] == '0': # idem mais de chaque coté du joueur
        b31()
    if tableau[y+1][x] == '0':
        b32()

def afficheMurOuest():
#background 0
    global x,y
    base()
    if x>2:
        if tableau[y+1][x-3] == '0':    # on cherche dans le tableau si la valeur( y-3, x-1) est 0 ALORS on affiche b01()
            b01()                     #  cela correspond à afficher le mur de gauche et qu'il y a 3 cases en face du joueur
        if tableau[y-1][x-3] == '0':
            b02()                    # cela correspond à afficher le mur de droite et qu'il y a 3 cases en face du joueur
        if tableau[y][x-3] == '0':
            b03()                   # cela correspond à afficher le mur au centre et qu'il y a 3 cases en face du joueur
    #background 1
    if x>1:
        if tableau[y+1][x-2] == '0': # idem 2 cases devant le joueur
            b11()
        if tableau[y-1][x-2] == '0':
            b12()
        if tableau[y][x-2] == '0':
            b13()
    #background 2
    if tableau[y+1][x-1] == '0':  # idem 1 case devant le joueur
        b21()
    if tableau[y-1][x-1] == '0':
        b22()
    if tableau[y][x-1] == '0':
        b23()
    #background 3
    if tableau[y+1][x] == '0': # idem mais de chaque coté du joueur
        b31()
    if tableau[y-1][x] == '0':
        b32()

def testDeplacement(touche):
    global x,y,d
    global startTempo
    if touche in ['a','z','e','q','s','d']:
        if (((touche == 'd' and d==0) or (touche == 'z' and d==1)or(touche == 'q' and d==2)or(touche == 's' and d==3)) and  tableau[y][x+1] == '1' ):
            x=x+1
        elif (((touche == 'z' and d==0) or (touche == 'q' and d==1)or(touche == 's' and d==2)or(touche == 'd' and d==3)) and  tableau[y-1][x] == '1' ):
            y=y-1
        elif (((touche == 'q' and d==0) or (touche == 's' and d==1)or(touche == 'd' and d==2)or(touche == 'z' and d==3)) and  tableau[y][x-1] == '1' ):
            x=x-1
        elif (((touche == 's' and d==0) or (touche == 'd' and d==1)or(touche == 'z' and d==2)or(touche == 'q' and d==3)) and  tableau[y+1][x] == '1' ):
            y=y+1
        elif touche == 'e':
            d=(d+1)%4
        elif touche == 'a':
            d=(d-1)%4
        if x == 3 and y == 11:
            tableau[13][8]='1'
            startTempo=time.clock()
            #print("match",startTempo)
        if x == 25 and y == 8:
            open("map2.csv", "r")

        afficheMurs()

def afficheMurs():
        if d==0:
            afficheMurNord()
            print("Nord",end=' ')
        if d==1:
            afficheMurEst()
            print("Est",end=' ')
        if d==2:
            afficheMurSud()
            print("Sud",end=' ')
        if d==3:
            afficheMurOuest()
            print("Ouest",end=' ')
        print(y,x)




def afficheCarte(positionX,positionY):
    for yCol in range(len(tableau)):
        for xLigne in range(len(tableau[0])):
            if (tableau[yCol][xLigne]=='0'):
                pygame.draw.rect(fenetre, NOIR, [positionX+xLigne*CARRE, positionY+yCol*CARRE, CARRE, CARRE])
            elif (tableau[yCol][xLigne]=='3'):
                pygame.draw.rect(fenetre, ROUGE,[positionX+xLigne*CARRE, positionY+yCol*CARRE, CARRE, CARRE])
            else:
                pygame.draw.rect(fenetre, BLANC, [positionX+xLigne*CARRE, positionY+yCol*CARRE, CARRE, CARRE])
    pygame.draw.rect(fenetre, VERT, [positionX+x*CARRE, positionY+y*CARRE, CARRE, CARRE])
            #print(tableau[y][x],end='')
        #print()

def WallButton():
    stopTempo=time.clock()
    #print(stopTempo-startTempo)
    if stopTempo-startTempo>10:
            tableau[13][8]='0'


afficheMurs()
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            testDeplacement(event.unicode)
            if event.key == pygame.K_ESCAPE or event.unicode == 'x': #touche x pour quitter
                loop = False
    # Actualisation de l'affichage
    WallButton()
    pygame.display.flip()

pygame.quit()
