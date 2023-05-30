#Ex13-timer
#Affiche l'heure dans un label toutes les secondes

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
from datetime import datetime   #import de la bibliothèque datetime

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex13-timer.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()             #affiche la fenêtre MainWindows

        self.cpt=0                  #initialise un compteur
        self.timer = QTimer(self)   #déclaration du timer
        self.timer.timeout.connect(self.miseAJour) #déclenche la méthode mise à jour
        self.timer.start(1000)      #toutes les secondes (1000ms)

    def miseAJour(self):
        self.cpt+=1         #incrémente le compteur
        print(self.cpt)     #affiche le compteur dans la console
        now = datetime.now()   #récupère la date et l'heure du PC
        heure = now.strftime("%H:%M:%S")    #formatage de l'heure
        self.label.setText(heure) #on change le nom du label avec l'heure


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()