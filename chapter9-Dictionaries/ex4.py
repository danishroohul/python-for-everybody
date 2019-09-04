# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

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

bigcount = None
bigword = None
for k,v in counts.items():
    if bigcount == None or v > bigcount:
        bigcount = v
        bigword = k

# Print output
print(bigword,bigcount)

