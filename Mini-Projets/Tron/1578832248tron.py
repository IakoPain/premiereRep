"""
Programme du tron
nom(s), prénom(s), classe(s)
"""
import pygame
from random import *

#constantes de la fenêtre d'affichage
LARGEUR=1024       #hauteur de la fenêtre
HAUTEUR=512#largeur de la fenêtre
NOIR=(0,0,0)
ROUGEFONCE=(128,0,0)
ROUGE=(255,0,0)
ORANGE=(255,128,0)
JAUNEFONCE=(128,128,0)
VERTCLAIR=(128,255,0)
JAUNE=(255,255,0)
VERT=(0,255,255)
BLEUVERT=(0,255,128)
BLEU=(0,128,128)
INDIGO=(0,128,255)
CYAN=(0,255,255)
BLEUFONCE=(0,0,255)
VIOLET=(128,0,255)
VIOLETFONCE=(128,0,128)
FUSHIA=(255,0,128)
FUSHIAFONCE=(255,0,255)
ROSE=(255,196,255)
BLANC=(255,255,255)



#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//4
motoY=LARGEUR//4
motoX2=768
motoY2=768/2
direction = 'bas'
direction2 = 'haut'

tempsPartie=0

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],1)
    for i in range(0,12):
        x=randint(0,1024)
        y=randint(0,512)
        pygame.draw.circle(fenetre, ROUGE, (x,y), 10)   #cercle plein aux coord x,y de rayon 10
    for i in range(0,12):
        x=randint(0,1024)
        y=randint(0,512)
        pygame.draw.rect(fenetre, INDIGO, [x, y, 10, 10],0)  #rectangle plein aux coord x,y

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond à une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision


def deplacementmoto():
    """
    deplace la moto si c'est possible
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX     #a completer
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX +1    #a completer
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), FUSHIA)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée

def deplacementmoto2():
    """
    deplace la moto si c'est possible
    """
    global motoX2,motoY2
    touche2=False
    if direction2=='haut2':
        x2=motoX2
        y2=motoY2-1
        touche=collisionMur2(x2,y2)
    elif direction2=='bas2':
        x2=motoX2     #a completer
        y2=motoY2+1
        touche2=collisionMur2(x2,y2)
    elif direction2=='droite2':
        x2=motoX2 +1    #a completer
        y2=motoY2
        touche2=collisionMur2(x2,y2)
    elif direction2=='gauche2':
        x2=motoX2-1
        y2=motoY2
        touche=collisionMur2(x2,y2)
    if touche2==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX2=x2
        motoY2=y2
    fenetre.set_at((x2, y2), VERT)
    return touche2#retourne la variable booleenne touche pour savoir si la partie est terminée

def deplacementmoto():
    global motoX,motoY
    x=1
    y=1
    """
    deplace la moto si c'est possible
    """

def deplacementmoto2():
    global motoX2,motoY2
    x2=1
    y2=1
    """
    deplace la moto si c'est possible
    """

    touche2=False
    if direction=='haut2':
        x=motoX2
        y=motoY2-1
        touche=collisionMur(x2,y2)
    elif direction=='bas2':
        x=motoX2     #a completer
        y=motoY2+1
        touche=collisionMur(x2,y2)
    elif direction=='droite2':
        x=motoX2 +1    #a completer
        y=motoY2
        touche=collisionMur(x2,y2)
    elif direction=='gauche2':
        x=motoX2-1
        y=motoY2
        touche=collisionMur(x2,y2)
    if touche2==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX2=x2
        motoY2=y2
    fenetre.set_at((x2, y2), ROUGE)
    return touche2          #retourne la variable booleenne touche pour savoir si la partie est terminée


loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE: #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction = 'gauche'
    if keys[pygame.K_z]:    #est-ce la touche UP
        direction2 = 'haut2'
    elif keys[pygame.K_s]:  #est-ce la touche DOWN
        direction2 = 'bas2'
    elif keys[pygame.K_d]:  #est-ce la touche RIGHT
        direction2 = 'droite2'
    elif keys[pygame.K_q]:  #est-ce la touche LEFT
        direction2 = 'gauche2'


    #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisé ici

    if deplacementmoto()==True:
        loop=False
    frequence.tick(120)
    pygame.display.update() #mets à jour la fenêtre graphique
    if deplacementmoto2()==True:
        loop=False
    frequence.tick(120)
    pygame.display.update()
    tempsPartie+=1
pygame.quit()
print('perdu')
print('temps partie',tempsPartie)


