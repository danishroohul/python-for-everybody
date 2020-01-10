import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_174820.html"
html = urllib.request.urlopen(url,context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

numbers = soup.find_all('span',{'class':'comments'})
l = []
for number in numbers:
    l.append(int(number.text))
print(sum(l))
