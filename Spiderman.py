import turtle

# Function to draw Spider-Man's face and upper body
def draw_spiderman():
    # Head
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.goto(20, 120)
    turtle.dot(10)
    turtle.goto(-20, 120)
    turtle.dot(10)

    # Body
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(80)
    turtle.setheading(-45)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(45)
    turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(80)

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Set up the Turtle
turtle.speed(0)  # Set the drawing speed to the fastest
turtle.hideturtle()  # Hide the Turtle

# Draw Spider-Man
draw_spiderman()

# Keep the window open
turtle.done()
