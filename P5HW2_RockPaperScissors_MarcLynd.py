# A variation of the classic rock, paper, scissors game created by Sam Kass and Karen Bryla
# called rock, paper, scissors, lizard, spock which became well known after appearing on the
# show "The Big Bang Theory"
# October 25, 2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Marc Anthony Lynd

# Import random to have access to the functions available within
import random
# def main
def main():

    # Create initial game variable to run at least once
    new_Game = "Y"
    
    # Display a header for the game being played
    print("Welcome to the game Rock, Paper, Scissors, Lizard, Spock\n")
    
    # Ask the user if they want to see how the game is played
    rules = input("Do you wish to see the rules of gameplay? Y or N: ")
    if rules == "Y" or rules == "y":
        game_Rules()

    else:
        ()
        
    # Call for get_UserName function
    user_Name = get_UserName()
    
    # Create a loop to allow for multiple game attempts and to quit when finished
    while new_Game == "Y" or new_Game == "y":

        # Start game
        print("Welcome",user_Name,"to the Rock Paper Scissors Lizard Spock Game\n")

        # Call for comp_Choice function
        compchoice = comp_Choice()

        # Call for num_Name function
        compConverted = num_Name(compchoice)

        # Call for user_Choice function
        userchoice = user_Choice()

        # Print the selection of both the user and computer
        print("You have chosen",userchoice,"and your opponent has chosen",compConverted)

        # Call for name_Number function
        userConverted = name_Number(userchoice)

        # Call for determineWinner function
        determineWinner(userConverted,compchoice)

        # Allow the new_Game variable to be altered to start again or quit
        new_Game = input("Would you like to play again, Y or N?")

# Define game_Rules function
def game_Rules():

    print("Game Rules")
    print("----------\n")
    print("Both you and your opponent will make a selection between:\nRock\nPaper\nScissors\nLizard\nor\nSpock\n")
    print("A winner will be determined by the comparison of you and your opponents selection\n")
    print("If both you and your opponent make the same selection it will be considered a draw and must be replayed in order to determine a winner\n")
    print("The following are the abilities of selections along with their vunerabilities:")
    print("Rock crushes Lizard")
    print("Rock crushes Scissors")
    print("Paper covers Rock")
    print("Paper disproves Spock")
    print("Scissors cuts Paper")
    print("Scissors decapitates Lizard")
    print("Lizard poisons Spock")
    print("Lizard eats Paper")
    print("Spock smashes Scissors")
    print("Spock vaporizes Rock")
    rules = input("Enter Q to exit: ")
    return rules
    
# Define get_UserName function and set parameter
def get_UserName():
    
    user_Name = input("Please enter your first name: ")
    return user_Name

# Define name_Number function and set parameter
# Assign a number for each possible name variable
def name_Number(userchoice):
    
    if userchoice == "Rock" or userchoice == "rock":
        return 0
    
    elif userchoice == "Paper" or userchoice == "paper":
        return 1
    
    elif userchoice == "Scissors" or userchoice == "scissors":
        return 2
    
    elif userchoice == "Lizard" or userchoice == "lizard":
        return 3
    
    elif userchoice == "Spock" or userchoice == "spock":
        return 4
    
    else:
        "Invalid Selection"

# Define num_Name function and set parameter
# Assign a name for each possible number variable
def num_Name(compchoice):
    
    if compchoice == 0:
        return "Rock"
    
    elif compchoice == 1:
        return "Paper"
    
    elif compchoice == 2:
        return "Scissors"
    
    elif compchoice == 3:
        return "Lizard"
    
    elif compchoice == 4:
        return "Spock"
    
    else:
        "Invalid Selection"

# Define comp_Choice function and set parameter
# Generates a random number for computers selection
def comp_Choice():
    
    compchoice = random.randrange(5)
    return compchoice

# Define user_Choice function and set parameter
# Displays available choices available to user
# Requests user to submit their selection
def user_Choice():
    
    print("Your Available Selections Are:\nRock\tPaper\tScissors\tLizard\tSpock\n")
    userchoice = input("Please enter your selection to play: ")
    return userchoice

# Compare the users entry and the selection of computer to determine winner, loser, or draw
def determineWinner(userConverted,compchoice):
    a = "Rock crushes Lizard"
    b = "Rock crushes Scissors"
    c = "Paper covers Rock"
    d = "Paper disproves Spock"
    e = "Scissors cuts Paper"
    f = "Scissors decapitates Lizard"
    g = "Lizard poisons Spock"
    h = "Lizard eats Paper"
    i = "Spock smashes Scissors"
    j = "Spock vaporizes Rock"
    

    if userConverted == 0 and compchoice == 3:
        print("Congradulations, Your",a)

    elif userConverted == 0 and compchoice == 2:
        print("Congradulations, Your",b)

    elif userConverted == 1 and compchoice == 0:
        print("Congradulations, Your",c)

    elif userConverted == 1 and compchoice == 4:
        print("Congradulations, Your",d)

    elif userConverted == 2 and compchoice == 1:
        print("Congradulations, Your",e)

    elif userConverted == 2 and compchoice == 3:
        print("Congradulations, Your",f)

    elif userConverted == 3 and compchoice == 4:
        print("Congradulations, Your",g)

    elif userConverted == 3 and compchoice == 1:
        print("Congradulations, Your",h)

    elif userConverted == 4 and compchoice == 2:
        print("Congradulations, Your",i)

    elif userConverted == 4 and compchoice == 0:
        print("Congradulations, Your",j)

    elif compchoice == 0 and userConverted == 3:
        print("Congradulations, Your",a)

    elif compchoice == 0 and userConverted == 2:
        print("Sorry, Your Opponents",b)

    elif compchoice == 1 and userConverted == 0:
        print("Sorry, Your Opponents",c)

    elif compchoice == 1 and userConverted == 4:
        print("Sorry, Your Opponents",d)

    elif compchoice == 2 and userConverted == 1:
        print("Sorry, Your Opponents",e)

    elif compchoice == 2 and userConverted == 3:
        print("Sorry, Your Opponents",f)

    elif compchoice == 3 and userConverted == 4:
        print("Sorry, Your Opponents",g)

    elif compchoice == 3 and userConverted == 1:
        print("Sorry, Your Opponents",h)

    elif compchoice == 4 and userConverted == 2:
        print("Sorry, Your Opponents",i)

    elif compchoice == 4 and userConverted == 0:
        print("Sorry, Your Opponents",j)

    else:
        print("It's a draw, you and your opponent have made the same selection")


    
main()
