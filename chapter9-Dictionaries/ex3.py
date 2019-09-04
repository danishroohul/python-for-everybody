# Exercise 3: Write a program to read through a mail log, build a histogram 
# using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

counts = dict()
people = list()
words = list()

# Open the file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("The file {} does not exist".format(fname))
    quit()

# Store the email-ids in a list
for line in fhandle:
    if not line.startswith("From "): continue
    words =  line.split()
    people.append(words[1])

# Make a histogram
for mails in people:
    counts[mails] = counts.get(mails,0) + 1

# Print output
print(counts)
