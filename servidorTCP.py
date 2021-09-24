import socket
import sys

#Se crea el Conector TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCP_IP = '127.0.0.1' 
TCP_PORT = 5005 #Puedes poner otro, verifica que no lo uses ya y que sea el mismo en el cliente tcp. 
BUFFER_SIZE = 2048 
