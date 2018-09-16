# Celsius to Fahrenheit Converter
# 09/10/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter
# Marc Anthony Lynd
#
#
# Ask the user to input a temperature in degrees Celsius which will be stored
# as the celsius variable
celsius = int(input("Please enter the Celsius temperature to be converted: "))
#
# Variable for Fahrenheit created from conversion formula and information
# gathered from user input
#
fahrenheit = 9/5*celsius + 32
#
# Add degree sign unicode along with the letter F to further show user that the 
# temperature is now being shown in degrees Fahrenheit
#
degree_signF = u'\N{DEGREE SIGN}F'
#
# Display for the user the converted temperature from Celsius to Fahrenheit
#
print ("Your Current Temperature is",fahrenheit,degree_signF)
#
# End of Program

