# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number
# of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.

emails = list()
counts = dict()

# Open file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("The file {} does not exist".format(fname))
    quit()

# Extract emails from the file
for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()
    emails.append(words[1])

# Create a histogram using dictionary
for mail in emails:
    counts[mail] = counts.get(mail,0) + 1

# Sort and get the highest person
most = [(val,ke) for (ke,val) in counts.items()] #List comprehension
most.sort(reverse = True)

# Print the output
k = most[0][1] # Key is the second element in our tuple
v = most[0][0] # Value is the first element in our tuple
print(k,v)

