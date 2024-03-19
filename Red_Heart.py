import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest
t.color("red")  # Set the color to red

# Draw the heart shape
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Hide the turtle and display the heart
t.hideturtle()
turtle.done()
