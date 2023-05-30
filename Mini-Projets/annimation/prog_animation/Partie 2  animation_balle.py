"""
Programme affichage
"""
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Affichage")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=2            #vecteur de déplacement
vecteurBalleY=1


def afficheBalle():
    """
    affiche un cercle aux coordonnées x,y avec un rayon
    """
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    """
    deplace la balle
    """
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX
    balleY=balleY+vecteurBalleY #on deplace la balle selon l'axeX

def testCollisionMurs():
    global vecteurBalleX,vecteurBalleY
    if balleX+RAYONBALLE>LARGEUR or balleX-RAYONBALLE<0:
        vecteurBalleX=vecteurBalleX*-1
    if balleY+RAYONBALLE>LARGEUR or balleY-RAYONBALLE<0:
        vecteurBalleY=vecteurBalleY*-1

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheBalle()
    deplacementBalle()
    testCollisionMurs()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()



