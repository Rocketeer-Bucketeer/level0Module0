import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
Hi_Turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
Hi_Turtle = turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
Hi_Turtle = turtle.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
Hi_Turtle = turtle.color('green')
Hi_Turtle = turtle.pencolor('blue')
# Move your turtle forward using .forward(100)
turtle.forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
turtle.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
for i in range (4):
    turtle.forward(100)
    turtle.left(90)

# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
turtle.goto(15, 15)
# x=0 and y=0 is the center of the screen

# Have your turtle draw a circle using .circle(radius, steps=30)
turtle.begin_fill()
turtle.circle(10, steps=30)
turtle.end_fill()
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle

# and .end_fill() below

# Draw 3 more shapes with different fill colors!
for i in range (3):
    turtle.circle(70, steps=30)


# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
