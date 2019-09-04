# Write a program which prompts the user for a Celsius temperature, 
#convert the temperature to Fahrenheit, and print out the converted temperature.

# Take user input
cel = float(input("Celsius Temperature: "))
far =  (( 9 / 5 ) * cel) + 32
far = round(far,2)
print("Fahrenheit Temperature:",far)
