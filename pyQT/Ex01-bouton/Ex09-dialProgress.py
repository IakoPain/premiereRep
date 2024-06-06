from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex09-dialProgress.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        self.dial.valueChanged.connect(self.potentiometre)
        self.pushButton.setStyleSheet("color: red")
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        self.dial.setValue(50)  #remets dial à 50

    def potentiometre(self):
        valeur=self.dial.value()    #récupère la valeur du dial
        print("Valeur =",valeur)
        self.progressBar.setValue(valeur)   #ajuste la barre de progression
        #changement de couleur progressive
        self.label.setStyleSheet( 'color: rgb({},0,0)'.format(valeur*255/100))
        #seuillage à 50 pour changer la couleur (valeur de la barre de progression)
        if valeur>50:
            self.progressBar.setStyleSheet("color: blue")
        else:
            self.progressBar.setStyleSheet("color: #00ff00")

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()
