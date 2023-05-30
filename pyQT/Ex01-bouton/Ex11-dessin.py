#Ex11-dessin
#tracer un point avec la souris
#détecter une touche au clavier

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex11-dessin.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()             #affiche la fenêtre MainWindows

        self.position = QPoint(0,0)

    def keyPressEvent(self, event): #une touche a été pressée
        key = event.key()
        if key == Qt.Key_M: #touche m ou M
            print("touche 'm' pressée")
        elif key == Qt.Key_Right:   #touche fleche droite
            print("touche droite pressée")

    def mousePressEvent(self, event):      #la souris est pressée
        self.position = QPoint(event.x(),event.y()) #récupère la position de la souris
        print(event.x(),event.y())  #affiche les coordonnées
        self.update()   #déclenche paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 5)) #definir un crayon
        painter.drawPoint(self.position)    #affciher un point aux coordonnées position

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()