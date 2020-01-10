import xml.etree.ElementTree as ET
import urllib.request
import ssl

url = input("Enter location: ")
if len(url) <1: url = "http://py4e-data.dr-chuck.net/comments_174822.xml"

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Retrieving ",url)

html = urllib.request.urlopen(url,context = ctx).read()
tree = ET.fromstring(html)

print("Retrieved",len(html),"characters")

numbers = tree.findall('comments/comment')

print("Count:",len(numbers))
ll = []
for number in numbers:
    ll.append(int(number.find("count").text))

print("Sum:",sum(ll))
