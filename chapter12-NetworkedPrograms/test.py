import socket
from bs4 import BeautifulSoup as soup

inp = input("Enter url (http://...): ")
if len(inp) < 1: inp = "http://data.pr4e.org/intro-short.txt"
url = inp.split('/')

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
    if len(data)<1: break
    data = soup(data)
    print(data,end=" ")
