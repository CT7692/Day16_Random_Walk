from turtle import Turtle, Screen, colormode
from random import randint


def turn_direction(tim_turtle):
    set_direction = randint(0, 1)
    if set_direction == 0:
        tim_turtle.right(randint(0, 90))
    elif set_direction == 1:
        tim_turtle.left(randint(0, 90))


def move_direction(tim_turtle):
    set_movement = randint(0, 1)
    if set_movement == 0:
        tim_turtle.forward(randint(25, 60))
    elif set_movement == 1:
        tim_turtle.backward(randint(25, 60))


colormode(255)
tim = Turtle()
tim.width(10)
my_screen = Screen()
for i in range(randint(20, 60)):
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    turn_direction(tim)
    move_direction(tim)
my_screen.exitonclick()
