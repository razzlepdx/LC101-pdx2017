#ch 5 exercises:
#############################

# 1 - Write a program that will use the turtle library to draw 5 evenly spaced, identical squares

#############################
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")
alex.penup()
alex.backward(100)
alex.pendown()

for i in range(5):
    drawSquare(alex,20)
    alex.penup()
    alex.forward(40)
    alex.pendown()

wn.exitonclick()
#########################

# 2 - Write a program to draw 5 nested boxes. Assume the innermost square is 20 units per side,
#and each successive square is 20 units bigger, per side, than the one inside it.

#########################

import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("pink")
side = 20

def drawSquare(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def rePosition(t):
    """Move turtle to starting position for next box - 135 degrees right and forward side(0.75)"""

    t.penup()
    t.right(135)
    t.forward(15)
    t.left(135)
    t.pendown()

for i in range(5):
    drawSquare(alex, side)
    side += 20
    rePosition(alex)

wn.exitonclick()

##########################

# 3- Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle
# draw a regular polygon.

##########################
import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
tess = turtle.Turtle()
tess.color("purple")

def drawPoly(someTurtle, somesides, somesize):
    for i in range(somesides):
        someTurtle.forward(somesize)
        someTurtle.left(360/somesides)

sides = int(input("How many sides on this polygon?"))
side_length = int(input("How long is each side?"))

drawPoly(tess, sides, side_length)

#############################

# 4 - Write a program that will draw a spiral at various angles.

#############################
import turtle

def drawSpiral(turtle, angle, length):
    for i in range(99):
        turtle.right(angle)
        tess.forward(length)
        length+=2

wn = turtle.Screen()
wn.bgcolor("light blue")
tess = turtle.Turtle()
tess.color("purple")
tess.speed(0)

side = 2
turn_angle = int(input("What is the angle of this spiral?"))

drawSpiral(tess, turn_angle, side)

###########################

# 5-

###########################

###########################

# 6 -  Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and
# including n.

############################
def sumTo(n):
    """returns the sum of all integers up to and including n"""
    return ((n * (n+1))// 2)

############################

# 11- rewrite the function sumTo(n) using the accumulator pattern.

############################

def sumTo(n):
    """returns the sum of all integers up to and including n"""
    for i in range(n):
        n += i
    return n

############################
