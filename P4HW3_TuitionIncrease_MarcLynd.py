# 3% increase to tuition every year for 5 years table
# October 6, 2018
# CTI-110 P4HW3 - Tuition Increase
# Marc Anthony Lynd
#
def tuitiontable():
    # Set defaults for variables
    originalTuition = 8000
    rateHike = (.03)
    year = 1
    # Print relevant data about the table
    print("Proposed tuition increase per year is ",(rateHike * 100),"% for the next 5 years", sep="")
    print("Current yearly tuition is: $",format(originalTuition,",.2f"), sep="")
    print()
    # Table formatting
    print("YEAR   \t\t\t   TUITION")
    print("====   \t\t\t   =======")
    # Initial year interst and tuition
    for year in range(1):
        tuitionIncrease = originalTuition * rateHike
        tuition = originalTuition + tuitionIncrease
        print("  ",year +1," - - - - - - - - - - -  $",format(tuition,(",.2f")), sep="")
        # Loop for compounded tuition increase
        for year in range(2,5+1):
            tuitionIncrease = tuition * rateHike
            tuition += tuitionIncrease
            print("  ",year," - - - - - - - - - - -  $",format(tuition, (",.2f")), sep="")
tuitiontable()
