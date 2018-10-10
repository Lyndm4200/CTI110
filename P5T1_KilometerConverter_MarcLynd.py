# Program that converts miles to kilometers
# October 10, 2018
# CTI-110 P5T1_KilometerConverter
# Marc Anthony Lynd
#

def ktomconv():
    # Ask user to input a distance in kilometers
    kilometers = float(input("Please input a distance in kilometers: "))
    
    if kilometers > 0:
        # Convert kilometers to miles
        miles = kilometers * 0.6214
        # Print output of conversion to user
        print("Your entered distance of ",kilometers,"km(s)is equal to ",format(miles,",.1f"),"mi(s)",sep='')
    # Create and error message if input is invalid   
    else:
        print("Error: Invalid Entry")
ktomconv()
