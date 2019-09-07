import socket

inp = input("Enter url (http://...): ")
url = inp.split('/')[2]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url,80))
    cmd = ("GET "+inp+" HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
except:
    print("URL not found")
    exit()
    
data = mysock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n')
print(message[header_end_pos:])    

while True:
    data = mysock.recv(512)
    if not data: break
    print(data.decode())
    
mysock.close()
