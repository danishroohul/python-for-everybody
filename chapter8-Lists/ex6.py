# Exercise 6: Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.


stuff = list()

# Main loop - take user input
while True:
    num = input("Enter a number: ")
    if num.lower() == 'done': break
    try: 
        num = float(num)
    except:
        print("Enter a valid number")
        continue
    stuff.append(num)

# Calculate the max and min
maximum = max(stuff)
minimum = min(stuff)

# Print the output
print("Maximum:",maximum)
print("Minimum:",minimum)
