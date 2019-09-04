# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

count = 0
total = 0

# Calculate total and count
while True:
    num = input("Enter a number: ")
    if num.lower() == 'done':
        break
    try:
        num = int(num)
    except:
        print("bad data")
        continue
    count = count + 1
    total = total + num
    
# Print total, count and average
average = total / count
print(total,count,average)
