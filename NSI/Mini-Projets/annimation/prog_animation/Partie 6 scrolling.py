"""
Programme de scrolling texte
"""
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=512       #hauteur de la fenêtre
HAUTEUR=512      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
COLOR=BLEU
scroll=100
#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Scrolling")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

texteX=LARGEUR
vectScroll=10


def afficheTexte(x,y,txt):
    global COLOR
    """
    affiche un texte aux coordonnées x,y
    """
    if scroll<0:
        COLOR=VERT
    if scroll>HAUTEUR:
        COLOR=ROUGE
    if texteX<-266:
        COLOR=BLEU
    texteAfficher = font.render(str(txt), True, COLOR)
    fenetre.blit(texteAfficher,(x,y))

def defilementTexte():
    global texteX,scroll,vectScroll
    scroll=scroll+vectScroll
    if scroll<0:
        vectScroll*=-1
    if scroll>HAUTEUR:
        vectScroll*=-1
    print(scroll)
    texteX-=10
    if texteX<-266:
        texteX=0



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False


    fenetre.fill((0,0,0))   #efface la fenêtre

    afficheTexte(texteX,scroll,'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
    defilementTexte()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()