# Staying in Budget or Not
# October 6, 2018
# CTI-110 P4HW1 - Budget Analysis
# Marc Anthony Lynd
#
def budget():
    # Ask user to input allocated funds for their monthly budget
    monthlyBudget = float(input("Please enter your available funds to budget for this month: "))
    # Set the totalExpense default to 0
    totalExpense = 0
    # Set the addexp default to "y" or "Y" to ensure the program runs at least once
    additionalExpense = "y"
    # Create a loop to ask the user if they have additional expenses to include in their budget
    while additionalExpense == "y" or additionalExpense == "Y":
        expense = float(input("Please enter your expense:$ "))
        totalExpense = totalExpense + expense
        additionalExpense = input("Y or N, Do you have another expense to include in this months budget: ")
    # Print the total expenses for the month to the user
    print("Your current total expenses for the month total $",format(totalExpense, ",.2f"))
    # Determine and inform the user if they are within their available budget or not and by how much
    if monthlyBudget >= totalExpense:
        underBudget = monthlyBudget - totalExpense
        print("You are within your desired budget, with an excess of $",format(underBudget, ",.2f"))
    else:
        overBudget = monthlyBudget - totalExpense
        print("You are overbudget by $",format(overBudget, ",.2f"))
budget()
