# Rewrite your pay computation with time-and-a-half for overtime
# (above 40 hours) and create a function called computepay which takes two parameters
# (hours and rate).

# Calculate the pay
def computePay(hours,rate):
    if hours > 40:
        pay1 = 40 * rate
        pay2 = (hours - 40) * rate * 1.5
        pay = pay1 + pay2
    else:
        pay = hours * rate
    return pay

# Take user input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Print the pay
Pay = computePay(hours,rate)
print("Pay:",Pay)
