# Question -Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL

'''Answer'''

import socket

# Taking User Input
inp = input("Enter url (http://...): ")
url = inp.split('/')

# Socket Connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((url[2],80))
    cmd = ("GET "+inp+" HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
except:
    print("URL not found")
    exit()

# Retreiving data   
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode(),end = " ")
   
# Closing connection
mysock.close()
