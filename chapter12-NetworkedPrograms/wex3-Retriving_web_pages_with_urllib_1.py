# Read a file on a website using urllib

'''Answer'''

import urllib.request as ur

# Access the data using urlopen function from urllib
fhandle = ur.urlopen('http://data.pr4e.org/romeo.txt')

# Print line by line by decoding the data from utf-8 to str
for line in fhandle:
    print(line.decode().strip())

