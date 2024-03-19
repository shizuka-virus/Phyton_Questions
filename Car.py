import turtle

def draw_car():
    # Car body
    turtle.penup()
    turtle.goto(-40, 0)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

    # Windows
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.end_fill()

    # Wheels
    turtle.penup()
    turtle.goto(-30, -20)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(20, -20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Set up the Turtle
turtle.speed(0)  # Set the drawing speed to the fastest
turtle.hideturtle()  # Hide the Turtle

# Draw the car
draw_car()

# Keep the window open
turtle.done()
