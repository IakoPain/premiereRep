#Ex06-comboBox
#Quand on clique sur le bouton, on affiche la ligne du comboBox choisi
#Dès que le combo box est changé, le label est rafraîchit

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex06-comboBox.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        #ajoute des items dans le combBox
        self.comboBox.addItems(["Six", "Nine", "Seven", "Eight", "negative_one", "owo"])
        #Quand on clique sur le combobox, on appelle la méthode selectionchange
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        choix=self.comboBox.currentText()
        print("Choix de l'utilisateur",choix)

    def selectionchange(self):
        choix=self.comboBox.currentText()
        self.label.setText(choix) #affiche le résultat dans le label


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()
