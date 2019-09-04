# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

counts = dict()
hours = list()

# Open the file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File {} does not exist".format(fname))
    quit()

# Extract hours from the file
for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()
    tim = words[5]
    hour = tim[0:2]
    hours.append(hour)

# Create a histogram of hours
for i in hours:
    counts[i] = counts.get(i,0) + 1

# Sort by hour
hsort =[(k,v) for (k,v) in counts.items()]
hsort.sort()

# Print the output
for i,j in hsort:
    print(i,j)

