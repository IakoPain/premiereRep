from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex10-graphics.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()             #affiche la fenêtre Main

#tous les exemples suivants seront mis dans la méthode paintEvent
    def paintEvent(self, event):
        painter = QPainter(self)
        #Affichage d'une image

        pic = QPixmap("logo.png") #chargement
        painter.drawPixmap(10,10, pic) #affichage aux

        painter.setPen(QPen(Qt.red, 5)) #definir un crayon
        painter.setBrush(Qt.green) # definir un remplissage
        painter.drawRect(100, 100, 200, 100) #tracé

        #tracé d'une ellipse
        painter.setPen(QPen(Qt.blue, 3)) #definir un crayon
        painter.setBrush(QColor(255, 255, 0)) #couleur de remplissage RGB
        painter.drawEllipse(90,30,130,40) #tracé

        #tracé de polygone
        points = [      #definir les 4 points du polygone
            QPoint(310,110),
            QPoint(310,200),
            QPoint(400,110),
            QPoint(400,200)
            ]
        painter.setPen(QPen(Qt.red, 5)) #crayon rouge largeur 5
        painter.setBrush(Qt.green) # couleur du remplissage
        poly = QPolygon(points) #instancier un polygone a partir de points
        painter.drawPolygon(poly)   #tracé

        #tracé de rectangle avec gradiant
        painter.setPen(QPen(Qt.black,  5, Qt.SolidLine))
        grad = QLinearGradient(10, 110, 50, 160)
        painter.setBrush(QBrush(grad))
        painter.drawRect(10, 110, 50, 160)

        #tracé de rectangle contour en pointillés
        painter.setPen(QPen(Qt.black,  5, Qt.DotLine)) #crayon noir largeur 5 en pointillés
        painter.setBrush(QBrush(Qt.red, Qt.CrossPattern)) #remplissage rouge
        painter.drawRect(210, 20, 260, 50) #tracé

        #Affichage de texte
        painter.setPen(QColor(255, 0, 0)) #couleur du crayon
        painter.setFont(QFont('Arial', 20)) #police
        painter.drawText(self.rect(), Qt.AlignCenter, "titi") #affichage au centre de la fenetre
        painter.drawText(300,300, "toto") #affichage aux coordonées

        #tracé de points
        painter.setPen(QColor(0, 0, 255)) #couleur du crayon
        for x in range(0,50,2):
            painter.drawPoint(x+10, 20)


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()