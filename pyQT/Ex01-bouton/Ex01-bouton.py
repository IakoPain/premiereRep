#Ex01-bouton
#Quand on clique sur le bouton, on change le nom du label par Bonjour

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex01-bouton.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la fonction boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        self.label.setText("owo") #on change le nom du label


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

