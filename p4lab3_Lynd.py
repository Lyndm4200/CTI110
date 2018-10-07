# Poor turtle forced to endure the cold and build a snowflake
# October 6, 2018
# CTI-110 P4T1c: Snowflake
# Marc Anthony Lynd
#
def snowflake():
    # Import turtle so tools are available to use
    import turtle
    win = turtle.Screen()
    anthony = turtle.Turtle()
    turtle.penup()
    turtle.pendown()
    # Set options to display the movement of turtle
    anthony.pensize(20)
    anthony.pencolor("blue")
    anthony.shape("turtle")
    # Set default
    move = 0
    a = 0
    b = 0
    c = 0
    d = 0
    # Get a starting location
    anthony.left(180)
    anthony.forward(0)
    # Loop for polygon
    for move in range(1,6+1):
        anthony.forward(50)
        anthony.right(60)
    # Set up for flake code
    anthony.forward(25)
    anthony.left(90)
    # Flake code
    for move in range(1,6+1):
        anthony.forward(200)
        for a in range(1,2+1):
            anthony.backward(10)
            anthony.right(45)
            anthony.forward(140)
            anthony.backward(140)
            anthony.left(90)
            anthony.forward(140)
            anthony.backward(140)
            anthony.right(45)
        for b in range(1,2+1):
            anthony.backward(20)
            anthony.right(45)
            anthony.forward(60)
            anthony.backward(60)
            anthony.left(90)
            anthony.forward(60)
            anthony.backward(60)
            anthony.right(45)
        for c in range(1,1+1):
            anthony.backward(40)
            anthony.right(45)
            anthony.forward(120)
            anthony.backward(120)
            anthony.left(90)
            anthony.forward(120)
            anthony.backward(120)
            anthony.right(45)
        anthony.backward(20)
        for d in range(1,4+1):
            anthony.backward(20)
            anthony.right(45)
            anthony.forward(30)
            anthony.backward(30)
            anthony.left(90)
            anthony.forward(30)
            anthony.backward(30)
            anthony.right(45)      
        anthony.right(90)
        anthony.forward(25)
        anthony.right(60)
        anthony.forward(25)
        anthony.left(90)
    win.mainloop()
snowflake()
