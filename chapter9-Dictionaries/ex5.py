# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

counts = dict()
words = list()
domains = list()

# Open the file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("The file {} doesn't exist".format(fname))
    quit()

# Extract domains from emails in the file
for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()
    mail = words[1]
    name,domain = mail.split('@')
    domains.append(domain)

# Create a histogram
for i in domains:
    counts[i] = counts.get(i,0) + 1

# Print output
print(counts)

