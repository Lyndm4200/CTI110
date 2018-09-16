# Sales Prediction
# 09/12/18
# CTI-110 P2T1 - Sales Prediction
# Marc Lynd
#
# Ask user to enter the projected total sales
#
ProjectedSales = float(input("Enter the projected sales total: "))
#
# Calculate profit of projected total sales by 23%
#
ProfitPrediction = ProjectedSales * 0.23
#
# Display the predicted profit to user
#
print ("Your estimated profit based on projected sales is $ ",
       format(ProfitPrediction,",.2f"))
#
# End of Program
