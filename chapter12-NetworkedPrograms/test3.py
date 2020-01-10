import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
max_count = int(input("Enter count: "))
position = int(input("Enter position: "))
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/known_by_Isak.html"
html = urllib.request.urlopen(url,context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

count = 0
while count < max_count:
    link = soup.find_all('a')[position-1].get('href')
    print("Retrieving: ",link)
    html = urllib.request.urlopen(link,context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    count = count + 1
