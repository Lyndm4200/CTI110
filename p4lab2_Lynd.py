# Poor turtle forced to draw my initials
# October 6, 2018
# CTI-110 P4T1b: Initials
# Marc Anthony Lynd
#
def initials():
    # Import turtle so tools are available to use
    import turtle
    win = turtle.Screen()
    anthony = turtle.Turtle()
    turtle.penup()
    turtle.pendown()
    # Set some default options to start out with for displaying turtle movement
    anthony.pensize(2)
    anthony.pencolor("blue")
    anthony.shape("turtle")
    # Set move default
    move = 0
    # Find a good starting point
    anthony.penup()
    anthony.backward(300)
    anthony.left(90)
    anthony.forward(100)
    anthony.right(90)
    anthony.pendown()
    # Drawing a rectangle
    for move in range(1,2+1):
        anthony.forward(600)
        anthony.right(90)
        anthony.forward(200)
        anthony.right(90)
    # Adjusting location and options
    anthony.penup()
    anthony.left(135)
    anthony.forward(20)
    anthony.right(135)
    anthony.pencolor("green")
    anthony.pensize(1)
    anthony.pendown()
    # Drawing a second rectangle outside the first
    for move in range(1,2+1):
        anthony.forward(630)
        anthony.right(90)
        anthony.forward(230)
        anthony.right(90)
    # Adjusting location and options
    anthony.penup()
    anthony.left(135)
    anthony.pencolor("purple")
    anthony.pendown()
    # Drawing first star
    for move in range(1,5+1):
        anthony.forward(50)
        anthony.right(144)
    # Adjusting location
    anthony.penup()
    anthony.left(135)
    anthony.forward(230)
    anthony.right(25)
    anthony.pendown()
    # Drawing second star
    for move in range(1,5+1):
        anthony.forward(50)
        anthony.right(144)
    # Adjusting location
    anthony.penup()
    anthony.left(115)
    anthony.forward(630)
    anthony.right(25)
    anthony.pendown()
    # Drawing third star
    for move in range(1,5+1):
        anthony.forward(50)
        anthony.right(144)
    # Adjusting location
    anthony.penup()
    anthony.left(115)
    anthony.forward(230)
    anthony.right(25)
    anthony.pendown()
    # Drawing fourth star
    for move in range(1,5+1):
        anthony.forward(50)
        anthony.right(144)
    # Adjusting location and options
    anthony.penup()
    anthony.left(115)
    anthony.forward(315)
    anthony.left(90)
    anthony.forward(35)
    anthony.pencolor("Gold")
    anthony.pensize(20)
    anthony.pendown()
    # Inputing initials, finally!!!!!!
    anthony.right(25)
    anthony.forward(175)
    anthony.backward(175)
    anthony.left(50)
    anthony.forward(175)
    anthony.backward(100)
    anthony.right(115)
    anthony.forward(65)
    anthony.backward(65)
    anthony.left(115)
    anthony.forward(100)
    anthony.left(65)
    anthony.penup()
    anthony.forward(80)
    anthony.left(90)
    anthony.forward(155)
    anthony.pencolor("red")
    anthony.pendown()
    anthony.backward(155)
    anthony.right(90)
    anthony.forward(120)
    anthony.penup()
    anthony.backward(550)
    anthony.left(70)
    anthony.pencolor("orange")
    anthony.pendown()
    anthony.forward(165)
    anthony.right(140)
    anthony.forward(90)
    anthony.left(140)
    anthony.forward(90)
    anthony.right(140)
    anthony.forward(165)
    win.mainloop()
initials()
