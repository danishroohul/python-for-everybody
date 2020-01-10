import urllib.request
import json
import ssl

url = input("Enter location: ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_174823.json"

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Retrieving ",url)

html = urllib.request.urlopen(url,context = ctx).read()
js = json.loads(html)
print("Retrieved",len(html),"characters")

ll = []
print("Count:",len(js["comments"]))
for item in js["comments"]:
    ll.append(int(item["count"]))

print("Sum:",sum(ll))
