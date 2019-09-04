# Question: Request data from a website

'''Answer'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creating a socket
mysock.connect(('data.pr4e.org',80))   # Connecting the socket through the port (80)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)    # Sending the request for the data

while True:
    data = mysock.recv(512)    # Receiving the data and storing in a variable
    if len(data) < 1:
        break
    print(data.decode(),end=' ')    # Print the data line by line

mysock.close()    # Closing the connection
