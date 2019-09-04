#Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

# Take user input
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    exit()

# Calculate pay
if hours <= 40:
    pay = hours * rate
else:
    pay1 = 40 * rate
    pay2 = (hours - 40) * rate * 1.5
    pay = pay1 + pay2

# Print pay
print("Pay:",pay)
