"""
Programme gestion de la souris
"""
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=255       #hauteur de la fenêtre
HAUTEUR=255     #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Balle")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=0            #vecteur de déplacement
vecteurBalleY=0


def afficheBalle():
    """
    affiche une balle aux coordonnées balleX,balleY avec un RAYON prédéfini
    """
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fenetre.fill((0,0,0))   #efface la fenêtre

    ROUGE=(balleX,balleY,(balleX+balleY)/2)
    balleX, balleY = pygame.mouse.get_pos()


    afficheBalle()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()



