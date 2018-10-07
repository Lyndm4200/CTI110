# Poor turtle forced to draw shapes
# October 6, 2018
# CTI-110 P4T1a: Shapes
# Marc Anthony Lynd
#
def shapes():
    # Import turtle so tools are available to use
    import turtle
    win = turtle.Screen()
    anthony = turtle.Turtle()
    turtle.penup()
    turtle.pendown()
    # Set options to display the movement of the turtle
    anthony.pensize(4)
    anthony.pencolor("green")
    anthony.shape("turtle")
    # Set default 
    move = 0
    # Loop for triangle
    for move in range(1,3+1):
        anthony.forward(120)
        anthony.left(120)
    # Pen up and moving turtle then pen down to seperate the shapes
    anthony.penup()
    anthony.right(90)
    anthony.forward(160)
    anthony.pendown()
    # Loop for square
    for move in range(1,4+1):
        anthony.forward(65)
        anthony.left(90)
    # Pen up and moving turtle for random effect
    anthony.penup()
    anthony.right(90)
    anthony.forward(160)
    # Victory Dance!!!
    for move in range(1,100+1):
        anthony.right(90)
        anthony.forward(10)
    win.mainloop()
shapes()
