# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

lstring = list()
counts = dict()

# Open file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("The file {} does not exist".format(fname))
    quit()

# Extract only alphabet from the file
ostring = fhandle.read()
for i in ostring:
    if not i.isalpha(): continue
    lstring.append(i.lower())

# Create a histogra of alphabet
for j in lstring:
    counts[j] = counts.get(j,0) + 1

# Sort the list alphabetically
orderr = [(k,v) for (k,v) in counts.items()]
orderr.sort()

# Print output
for (a,b) in orderr:
    print(a,b)

