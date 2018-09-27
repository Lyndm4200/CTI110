# CTI-110
# P3LAB - Debugging
# Marc Lynd
# September 27, 2018

def main():
    # This program takes a number grade and outputs a letter grade.
    # System uses 10-point grading scale
    # Get number grade from user and save to variable 'score'
    score = float(input("Enter number grade: "))
    # Calculate the grade letter based on number entered
    if score >= 90 and score <= 100:
        print("Your grade is A")
    elif score >= 80 and score < 90:
        print("Your grade is B")
    elif score >= 70 and score < 80:
        print("Your grade is C")
    elif score >= 60 and score < 70:
        print("Your grade is D")
    elif score < 60:
        print("Your grade is F")
    # Error message if number entered is not within the grading scale
    else:
        print("ERROR: NUMBER ENTERED IS INVALID")

main()
# End of Program
