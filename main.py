import turtle
import random
import colorgram
from turtle import Turtle, Screen

my_turtle = Turtle()
turtle.colormode(255)
my_turtle.shape("turtle")
my_turtle.width(20)

my_turtle.speed("fastest")
my_screen = Screen()
width = my_screen.window_width()
height = my_screen.window_height()

color_tuples = []
holder = 3
wrapper = 1

def turtle_check_direction(move_counter):
    if move_counter == holder:
        return True


for x in colorgram.extract("PythonArt.png", 500):
    color_tuples.append((x.rgb.r, x.rgb.g, x.rgb.b))

tuple_holder = color_tuples.copy()
print(color_tuples)

# Start in center, spiral out at right angles until out of colors

#super cool semi-solution below
# counter = 0
# for color in color_tuples:
#     counter += 1
#     my_turtle.color(color)
#     my_turtle.pendown()
#     my_turtle.forward(0)
#     my_turtle.penup()
#     if turtle_check_direction(counter):
#         for x in range(wrapper):
#             my_turtle.forward(50)
#             my_turtle.pendown()
#             my_turtle.forward(0)
#             my_turtle.penup()
#         counter = 0
#         wrapper += 1
#     my_turtle.right(90)
#     my_turtle.forward(50)

#Almost Real Spiral solution
# bank = 0
# turn_holder = 0
# lengthen = 1
# passes = 0
#
# for x in range(6):
#     for color in tuple_holder:
#         color_tuples.append(color)
#
# for x in range(len(color_tuples)):
#     my_turtle.color(color_tuples[x])
#     my_turtle.pendown()
#     my_turtle.forward(0)
#     my_turtle.penup()
#     my_turtle.forward(50)
#     bank += 1
#     if (bank >= 1):
#         my_turtle.right(90)
#         turn_holder += 1
#         passes += 1
#         if turn_holder >= 1:
#             bank = (-1 * lengthen)
#             if passes == 2:
#                 passes = 0
#                 lengthen += 1
#             turn_holder = 0
#     print(x, len(color_tuples))

#real solution

my_turtle.hideturtle()
my_turtle.penup()
my_turtle.right(180)
my_turtle.forward((my_screen.window_width()/2)-50)
my_turtle.left(90)
my_turtle.forward((my_screen.window_height()/2)-50)
my_turtle.left(90)

def turtle_move():
    my_turtle.pendown()
    my_turtle.forward(0)
    my_turtle.penup()
    my_turtle.forward(50)

# Turtle is now positioned in the bottom left, facing right

count = 0
for x in range(int(my_screen.window_height()/50)):
    for y in range(int((my_screen.window_width()-100)/50)):
        my_turtle.color(color_tuples[count % len(color_tuples)])
        my_turtle.pendown()
        my_turtle.forward(0)
        my_turtle.penup()
        my_turtle.forward(50)
        count += 1
    if not x % 2:
        my_turtle.left(90)
        turtle_move()
        my_turtle.left(90)
    else:
        my_turtle.right(90)
        turtle_move()
        my_turtle.right(90)

my_turtle.forward(100)


my_screen.exitonclick()
