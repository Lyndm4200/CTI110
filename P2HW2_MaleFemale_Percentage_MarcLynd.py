# Display the percentage of Males v. Females registered in a class
# 09/10/2018
# CTI-110 P2HW2 - Male Female Percentage
# Marc Anthony Lynd
#
# Ask the user to input the number of male students registered for a class
#
male = int(input("How many male students are registered for the class?: "))
#
# Ask the user to input the number of female students registered for the class
#
female = int(input("How many female students are registered for the class?: "))
#
# Find the common variable that will connect the two groups, total students
#
students = male + female
#
# Create the operation/variable for percentage of males
#
malepercent = male / students
#
# Create the operation/variable for percentage of females
#
femalepercent = female / students
#
# Display the percentage of male and female students registered for the class
#
print ("Males Registered for the Class -- ","{0:.2f}%".format(malepercent * 100))
print ("Females Registered for the Class -- ","{0:.2f}%".format(femalepercent * 100))
#
# End of Program
