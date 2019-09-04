import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((HOST,PORT))
mysock.sendall('
