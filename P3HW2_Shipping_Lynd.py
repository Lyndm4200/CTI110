# CTI-110
# P3HW2 - Shipping Charges
# Marc Lynd 
# September 26, 2018
#
# Ask user to input the weight of the package
packageWeight = float(input("Please enter the exact weight of the package: "))
# Determine shipping tier, calculate, display results to user
if packageWeight <=2:
    packageChargeTierOne = packageWeight * 1.5
    print("Your total shipping charges are: $",format(packageChargeTierOne, ".2f"))
elif packageWeight > 2 and packageWeight <= 6:
    packageChargeTierTwo = packageWeight * 3
    print("Your total shipping charges are: $",format(packageChargeTierTwo, ".2f"))
elif packageWeight > 6 and packageWeight <= 10:
    packageChargeTierThree = packageWeight * 4
    print("Your total shipping charges are: $",format(packageChargeTierThree, ".2f"))
else:
    packageChargeTierFour = packageWeight * 4.75
    print("Your total shipping charges are: $",format(packageChargeTierFour,".2f"))
#
# End of program
