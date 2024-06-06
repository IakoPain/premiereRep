#Chat texte en UDP sans QUdpSocket

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import socket

UDP_IP_DU_BINOME = "172.18.49.134"   #adresse du client (la machine du binôme) à adapter
UDP_PORT_DU_BINOME = 5001        #port du client (la machine du binôme) à adapter
UDP_IP_MON_PC = "172.18.50.163"   #adresse de mon serveur
UDP_PORT_MON_PC = 5001        #port de mon serveur

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('visuel.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()                     #affiche la fenêtre MainWindows

        self.pushButton.clicked.connect(self.boutonEnvoi)
        self.timer = QTimer(self)   #déclaration du timer
        self.timer.timeout.connect(self.miseAJour) #déclenche la méthode mise à jour
        self.timer.start(100)      #toutes les secondes (100ms)

    def miseAJour(self):
        try:
            octets, server = sock.recvfrom(1024)
        except socket.error as msg:
            octets=None
        if octets!=None:
            message=octets.decode()
            print('reception :',message)
            self.listWidget.insertItem(0, message)
            self.listWidget.item(0).setForeground(QtCore.Qt.red)

    def boutonEnvoi(self):
        msg=self.lineEdit.text()
        print('texte envoyé')
        octets=msg.encode("UTF8")
        print(octets)
        sock.sendto(octets, (UDP_IP_DU_BINOME, UDP_PORT_DU_BINOME))

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()