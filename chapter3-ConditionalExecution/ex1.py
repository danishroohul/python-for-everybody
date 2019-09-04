# Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.

# Take user input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Pay calculation
if hours <= 40:
    pay = hours * rate
else:
    pay1 = 40 * rate
    pay2 = (hours - 40) * rate * 1.5
    pay = pay1 + pay2

# Print output
print("Pay: ",pay)
