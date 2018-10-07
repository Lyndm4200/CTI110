# Poor turtle forced create shapes with nested loops
# October 7, 2018
# CTI-110 P4LAB: Nested Loops
# Marc Anthony Lynd
#
def nestedloops():
    # Import turtle so tools are available to use
    import turtle
    win = turtle.Screen()
    anthony = turtle.Turtle()
    turtle.penup()
    turtle.pendown()
    # Set options to display movement of the turtle
    anthony.pensize(10)
    anthony.pencolor("gold")
    anthony.shape("turtle")
    # Set default variables
    move = 0
    a = 0
    b = 0
    c = 0
    d = 0
    # Get a starting location
    anthony.penup()
    anthony.backward(50)
    anthony.right(90)
    anthony.forward(150)
    anthony.left(90)
    anthony.pendown()
    # Create a nested loop that will use triangles to form a inner dodecagon
    for move in range(1,12+1):
        # Nested Triangle loop
        for a in (1,2,3):
            anthony.forward(100)
            anthony.right(120)
        anthony.forward(100)
        anthony.left(30)
    # Set up location for next loop
    anthony.penup()
    anthony.left(90)
    anthony.forward(235)
    anthony.right(90)
    anthony.forward(35)
    anthony.pendown()
    # Next loop
    for b in range(1,12+1):
        anthony.pencolor("red")
        anthony.forward(100)
        anthony.right(120)
        anthony.forward(100)
        anthony.left(330)
        
    win.mainloop()
nestedloops()
