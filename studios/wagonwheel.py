#studio for class 4-24-17
###############

# Write a program using the turtle module to draw a spiral foursquare pattern

###############
import turtle

#initialize turtle and screen settings
alex = turtle.Turtle()
alex.speed(0)
alex.color("blue")
alex.pensize(2)

wn = turtle.Screen()
wn.bgcolor("light green")

def draw_square(length):
    '''draws a single square - turtle ends in the direction of the last line drawn'''
    for i in range(3):
        alex.forward(length)
        alex.left(90)
    alex.forward(length)

def draw_foursquare(length):
    '''draws the square 4 times, to make a foursquare pattern'''
    for i in range(4):
        draw_square(length)

def draw_spiral(length, angle):
    '''draws a foursquare, then turns the turtle and repeats 5 times to create a spiral pattern'''
    for i in range(5):
        draw_foursquare(length)
        alex.left(angle)

draw_spiral(90, int(90/5))
