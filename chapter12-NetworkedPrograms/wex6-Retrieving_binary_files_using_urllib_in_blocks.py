import urllib.request as req

img = req.urlopen("http://data.pr4e.org/cover3.jpg")
fhand = open("cover32.jpg","wb")
size = 0

while True:
    info = img.read(100000)
    if len(info)<1:break
    size = size + len(info)
    fhand.write(info)
    
print(size,'Characters copied')
fhand.close()
