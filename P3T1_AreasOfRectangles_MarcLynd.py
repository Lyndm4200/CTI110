# Comparing Areas of Rectangles
# September 26,2018
# CTI_110 Tutorial P3T1 - Areas of Rectangles
# Marc Lynd
#
# Ask user to input length and width of rectangle 1
rectLenghth_1 = float(input("Please enter the length of the first rectangle: "))
rectWidth_1 = float(input("Now enter the width: "))
# Ask user to input length and width of rectangle 2
rectLenghth_2 = float(input("Please enter the length of the second rectangle: "))
rectWidth_2 = float(input("Now enter the width: "))
# Calculate area of rectangle 1
rectArea_1 = rectLenghth_1 * rectWidth_1
# Calculate area of rectangle 2
rectArea_2 = rectLenghth_2 * rectWidth_2
# Compare area of rectangles and display which has the greatest area or if they
# have the same area
if rectArea_1 > rectArea_2:
    print("The first rectangle has the largest area")
elif rectArea_1 < rectArea_2:
    print("The second rectangle has the largest area")
else:
    print("Both rectangles have an equal area")
#
# End of Program
