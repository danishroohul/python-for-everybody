# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average.

import re

numb = list()
full = list()
count = 0

# Open file
fname = input("Enter file: ")
try:
    fhandle = open(fname)
except:
    print("The file {} does not exist".format(fname))
    quit()

# Extract lines that contain "New Revision"
for line in fhandle:
    if not re.search('^New Revision: ',line): continue
    numb = re.findall('^New Revision: ([0-9]+)',line)
    full.append(float(numb[0]))
    count = count + 1

# Print Average
s = sum(full)
print(s/count)
