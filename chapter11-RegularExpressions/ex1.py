# Exercise 1: Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:

import re

count = 0

# Open the file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print('The file {} does not exist'.format(fname))
    quit()

# Take the regular expression input
regu = input('Enter a regular expression: ')

# Count the number of lines that matched the regular expression
for line in fhandle:
    if not re.search(regu,line): continue
    count = count + 1

# Print output
print("{} had {} lines that matched {}".format(fname,count,regu))
