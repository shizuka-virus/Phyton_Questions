import turtle
import math

# Set up the screen
wn = turtle.Screen()
wn.title("Pumping Heart")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create a heart shape
def create_heart():
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.hideturtle()
    return t

# Draw a heart using the given turtle object and scale
def draw_heart(t, scale):
    t.penup()
    t.goto(16 * scale, 100 * scale)
    t.pendown()
    t.begin_fill()
    t.left(50)
    t.forward(100 * scale)
    t.circle(40 * scale, 180)
    t.right(90)
    t.circle(40 * scale, 180)
    t.forward(100 * scale)
    t.end_fill()

# Calculate the y-coordinate of a point on a sine wave given the x-coordinate and time
def sine_wave(x, t, amplitude, frequency):
    return amplitude * math.sin(frequency * x - t)

# Animate the heart pumping
def animate_pumping_heart(heart):
    scale = 2
    amplitude = 15
    frequency = 0.05
    t = 0

    while True:
        # Clear the previous drawing
        heart.clear()
        
        # Draw the heart at the current position
        draw_heart(heart, scale)

        # Calculate the y-coordinate for the next frame
        y_offset = sine_wave(0, t, amplitude, frequency)
        
        # Move the heart up or down based on the y-coordinate
        heart.penup()
        heart.sety(heart.ycor() + y_offset)
        heart.pendown()
        
        # Update time for next frame
        t += 0.1

# Create the heart object
heart = create_heart()

# Start animating the pumping heart
animate_pumping_heart(heart)

# Close the window when clicked
wn.mainloop()
