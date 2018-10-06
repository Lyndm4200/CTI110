# A Celsius to Fahrenheit converter in table format
# October 6, 2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Marc Anthony Lynd
#
def ctofconv():
    # Set up celsius default and optional degree indicators for both celsius and fahrenheit
    degreeSignC = "\N{DEGREE SIGN}C"
    degreeSignF = "\N{DEGREE SIGN}F"
    celsius = 0
    # Set up table headers
    print("Celsius\t    Fahrenheit")
    print("-------     ----------")
    # Designate "for" and "range" output for celsius
    for celsius in range (0,20+1):
        # Calculation for fahrenheit conversion based on range output of celsius
        fahrenheit = float(format(32 + (9/5 * celsius),"0.1f"))
        # Print conversions to table
        print(celsius,degreeSignC,"\t   ",fahrenheit,degreeSignF)
ctofconv()
