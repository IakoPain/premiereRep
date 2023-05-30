#Ex02-bouton

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex02-texte.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        txt=self.lineEdit.text()    #récupère le texte de lineEdit
        print('texte saisi:',txt,type(txt)) #affiche le texte et le type
        if txt.isnumeric():     #le texte est-il un chiffre ?
            a=int(txt)          #conversion en entier
            a=a+20              #ajoute 20
            self.label.setText(str(a)) #affiche le résultat en chaîne de caractères
        else:
            self.label.setText("nombre svp")



app = QApplication(sys.argv)
window = MainWindows()
app.exec_()
