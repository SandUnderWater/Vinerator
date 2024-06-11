import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create a turtle
green_turtle = turtle.Turtle()
green_turtle.color("green")
green_turtle.speed("fastest")

# Define a function to draw a random green line
def draw_green_line():
    length = random.randint(50, 200)
    tilt_angle = random.randint(-300, 300)
    green_turtle.forward(length)
    green_turtle.left(90 + tilt_angle)

# Draw multiple green lines within the screen boundaries
for _ in range(4000):
    x, y = green_turtle.pos()
    if abs(x) < 400 and abs(y) < 300:
        draw_green_line()
    else:
        # Respawn in the middle
        green_turtle.goto(0, 0)
        green_turtle.setheading(random.randint(0, 360))
        draw_green_line()

# Hide the turtle cursor
green_turtle.hideturtle()

# Keep the window open until manually closed
turtle.done()
