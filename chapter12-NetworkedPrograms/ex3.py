# Question - Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

'''Answer'''

import urllib.request as request

# Take user input
url = input("Enter url (http://...): ")

# Requesting data from the website
try:
    fhandle = request.urlopen(url)
except:
    print("URL not found")
    exit()

# Printing till 3000 characters
count = 0
for line in fhandle:
    lin = line.decode().strip()
    if len(lin) + count >= 3000:
        print(lin[:(3000-count)])
        exit()
    else:
        print(lin)
    count = count + len(lin)
    
