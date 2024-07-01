from turtle import Turtle, Screen, colormode
import secrets

colormode(255)


def random_color(tim_turtle):
    r = secrets.SystemRandom().randint(0, 255)
    g = secrets.SystemRandom().randint(0, 255)
    b = secrets.SystemRandom().randint(0, 255)
    return tim_turtle.color(r, g, b)


def turn_direction(tim_turtle):
    set_direction = secrets.SystemRandom().randint(0, 1)
    if set_direction == 0:
        tim_turtle.right(secrets.SystemRandom().randint(0, 90))
    elif set_direction == 1:
        tim_turtle.left(secrets.SystemRandom().randint(0, 90))


def move_direction(tim_turtle):
    set_movement = secrets.SystemRandom().randint(0, 1)
    if set_movement == 0:
        tim_turtle.forward(secrets.SystemRandom().randint(25, 60))
    elif set_movement == 1:
        tim_turtle.backward(secrets.SystemRandom().randint(25, 60))


tim = Turtle()
tim.width(10)
my_screen = Screen()
for i in range(secrets.SystemRandom().randint(80, 200)):
    random_color(tim)
    turn_direction(tim)
    move_direction(tim)
my_screen.exitonclick()
