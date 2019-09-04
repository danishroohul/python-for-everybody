# Count the number of times each word is repeated in the file over the internet

'''Answer'''

import urllib.request

# Access the file from the website
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Count the word occurances line wise
counts = dict()
size = 0
for line in fhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        if size<len(word):
            size = len(word)

# Print output
print(counts,end="\n\n")

# Extra: print like a grocery list XD
for i,j in counts.items():
    s = i.ljust(size)+" : "+str(j)
    print(s)
