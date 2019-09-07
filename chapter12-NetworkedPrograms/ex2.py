# Question - Exercise 2: Change your socket program so that it counts the number 
# of characters it has received and stops displaying any text after it has shown 
# 3000 characters. The program should retrieve the entire document and count the 
# total number of characters and display the count of the number of characters at 
# the end of the document

'''Answer'''

import socket

inp = input("Enter url (http://...): ")
url = inp.split('/')

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url[2],80))
    cmd = ("GET "+inp+" HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
except:
    print("URL not found")
    exit()

count = 0
while True:
    data = mysock.recv(1000)   # Number inside the paranthesis is the amount of characters that is requested per loop
    if len(data) < 1: break
    count = count + len(data)
    #print(len(data),count)
    print(data.decode(),end = "")
    if count >= 3000: break
    
mysock.close()

