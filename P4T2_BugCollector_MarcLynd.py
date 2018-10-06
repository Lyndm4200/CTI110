# Keep a running total of bugs collected over 5 days
# October 6, 2018
# CTI-110 P4T2 - Bug Collector
# Marc Lynd
#
def buggy():
    # Set default variables
    bugs = 0
    totalBugs = 0
    # Start loop for 5 days
    for bugs in range(1,5+1):
        # Asks for user input each day
        bugsCollected = int(input("Please enter the amount of bugs collected today: "))
        # Saves the user input for each day and continues to add to it as the days accumulate
        totalBugs += bugsCollected
    # Print output for the five days
    print("You have collected a total of", format(totalBugs,","),"bugs in the past 5 days")
buggy()
