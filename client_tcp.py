# ...existing code...
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.20.61.12', 10000)  # remplacer par l'IP de l'ESP si différente
print('Connexion TCP a %s sur le port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send command to toggle LED
    message = 'LED ON'  # ou 'LED OFF'
    print('Envoi de : "%s"' % message)
    sock.sendall((message + '\n').encode())
    
    # Wait for response (single line)
    data = sock.recv(255)
    if data:
        print('Recu :  "%s"' % data.decode().strip())

finally:
    print('Fermeture du socket TCP')
    sock.close()
# ...existing code...