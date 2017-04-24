#Chapter 4 Exercises

#Write a program that prints "We like Python's turtles!" 1000 times

for x in range(1000):
    print("We like Python's turtles!")

#Write a program that prints out the lyrics to the song "99 bottles of beer on the wall"

for num in range(99, 0 ,-1):
    print(num, "Bottles of Beer on the wall,", num, "bottles of beer!")
    if num - 1 == 0:
        print("Take one down, pass it around, no more bottles of beer on the wall!")
    else:
        print("Take one down, pass it around,", (num - 1), "bottles of beer on the wall!")

#Write a program that uses a for loop to print "One of the months of the year is January"
#/"One of the months of the year is February"/ "One of the months of the year is March", etc

for month in("January", "February", "March", "April", "May", "June", "July", "August", "September",
"October", "November", "December"):
    print("One of the months of the year is", month)

#Use for loops to make a turtle draw these regular polygons: equilateral triangle, square, hexagon, octagon

import turtle
wn = turtle.Screen()

#turtle Tina draws an equilateral Triangle
tina = turtle.Turtle()
tina.color("light blue")

for i in range(3):
    tina.forward(70)
    tina.left(120)

#turtle Bruce draws a square
bruce = turtle.Turtle()

for i in range(4):
    bruce.left(90)
    bruce.forward(100)

#turtle Julie draws a hexagon
julie = turtle.Turtle()
julie.color("green")
julie.pensize(4)

for i in range(6):
    julie.forward(25)
    julie.right(60)

#turtle Ivan draws an octagon
ivan = turtle.Turtle()
ivan.color("red")
ivan.pensize(3)

for i in range(8):
    ivan.backward(80)
    ivan.left(45)

wn.exitonclick()

#Write a program that asks the user for the number of sides, the length of the side, the color,
#and the fill color of a regular polygon.  The program should draw the polygon and fill it in.

#import turtle and create screen
import turtle
wn = turtle.Screen()

#get user input to determine shape and colors to be drawn
sides = input("How many sides in this polygon?")
length = input("what is the length of each side?")
color = input("What color is each side of this shape?")
fill_color = input("How about the fill color?")

#convert number and length of sides from strings to ints
sides = int(sides)
length = int(length)

#create turtle and assign colors according to user input
shapely = turtle.Turtle()
shapely.color(color, fill_color)

#tell turtle to begin fill color process
shapely.begin_fill()

#draw shape based on user input
for i in range(sides):
        shapely.forward(length)
        shapely.left(360/sides)

#after drawing is completed, tell turtle to stop color fill process, and click to exit screen.
shapely.end_fill()

wn.exitonclick()


#Write a turtle program that maps the path walked by a drunken pirate.  After the pirate is done
#walking, print the current heading.

import turtle
wn = turtle.Screen()

pirate = turtle.Turtle()
data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for direction in data:
    pirate.left(direction)
    pirate.forward(100)

print("The pirate's final heading was", pirate.heading())

wn.exitonclick()

#Write a program to draw a star shape:

import turtle
wn = turtle.Screen()

star = turtle.Turtle()
star.pensize(2)

for i in range(5):
    star.right(144)
    star.forward(70)

wn.exitonclick()




#weekly Graded assignment

#Assume you have the list of numbers nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#write a loop that prints each of the numbers on a new line
#write a second loop that prints each number and it's square on a new line, ex: The square of 12 is
#144 \n the square of 10 is 100, etc

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in nums:
  print(num)

for num in nums:
  print("The square of", num, "is", (num**2))
