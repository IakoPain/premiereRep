#serveur UDP (CTRL+F2 pour stopper)
import socket

UDP_IP_MON_PC = "172.18.50.163"   #adresse de mon serveur
UDP_PORT_MON_PC = 5000        #port de mon serveur

# Crée un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

boucle=True
while(boucle):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data=None
            continue
        print ('received ', data)
        if (data.decode()=='q'):
            boucle=False
print('closing socket')
sock.close()