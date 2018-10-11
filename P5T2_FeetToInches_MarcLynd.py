# Create a function to be used in a program
# October 11, 2018
# CTI-110 P5T2_FeetToInches
# Marc Anthony Lynd
#
def main():
    # Ask user to input feet to be converted
    feet = float(input("Please enter the amount of feet you wish to be converted to inches: "))
    # Call, format, and print function out to user
    print(format(feet_to_inches(feet),",.2f"))      
# Function created for conversion
def feet_to_inches(feet):
    return feet * 12
main()
