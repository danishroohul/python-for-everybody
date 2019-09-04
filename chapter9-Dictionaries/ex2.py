# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

days_of_week  = list()
counts = dict()

# Open the file
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("The file {} does not exist, try again".format(fname))
    quit()

# Store the days of the week the mail received 
for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()
    days_of_week.append(words[2])

# Count the number of commits done on that day of the week
for day in days_of_week:
    counts[day] = counts.get(day,0) + 1

# Print the output
print(counts)
