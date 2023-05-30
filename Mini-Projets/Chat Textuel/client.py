#client UDP
import socket

UDP_IP_DU_BINOME = "172.18.49.134"   #adresse de la machine du binôme (à adapter)
UDP_PORT_DU_BINOME = 5000        #port de la machine du binôme (à adapter)

# Crée un socket UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = '<message>'
octets = message.encode("Utf8")
print(octets)
sock.sendto(octets, (UDP_IP_DU_BINOME, UDP_PORT_DU_BINOME))