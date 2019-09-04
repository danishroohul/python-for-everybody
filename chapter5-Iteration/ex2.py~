# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

count = 0
total = 0
big = None
smol = None

while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    else:
        try:
            number = int(number)
        except:
            print("Bad data")
            continue
        if big == None:
            big = number
        elif number > big:
            big = number
        if smol == None:
            smol = number
        elif number < smol:
            smol = number
        count = count + 1
        total = total + number

print(total,count,big,smol) 
