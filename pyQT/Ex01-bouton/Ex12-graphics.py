#Ex12-graphics
#tracé de formes géométriques

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex12-graphics.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.scene = QGraphicsScene(self) #instancie un scene
        self.brush= QBrush(Qt.lightGray)  #couleur de remplissage
        self.pen = QPen()                  #crayon
        #implante la scene dans la vue graphique
        self.scene.setSceneRect(0, 0, self.graphicsView.width(), self.graphicsView.height())
        #couleur de fond
        self.scene.setBackgroundBrush(self.brush)
        self.graphicsView.setScene(self.scene)
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        self.pen.setWidth(2)
        self.brush.setColor(Qt.red)
        self.scene.addLine(0,0,50,200,self.pen)
        self.scene.addRect(30,30, 50,50,self.pen,self.brush)
        #lst=self.scene.items()
        #self.scene.removeItem(lst[1])
        self.font=QFont("Fixed",20)
        self.texte = self.scene.addText("uwu",self.font)
        self.texte.setDefaultTextColor(Qt.blue)
        self.texte.setPos(50,100)

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()