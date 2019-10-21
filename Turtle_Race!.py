# Turtle Race!
import turtle
import random

wn = turtle.Screen()
wn.setup(width=0.80, height=0.5, startx=None, starty=None)
wn.bgcolor("hotpink")

pepps = turtle.Turtle()
pepps.shape("turtle")
pepps.color("blue")

mary = turtle.Turtle()
mary.shape("turtle")
mary.color("green")

pepps.up()
pepps.goto(-500, 20)
pepps.write("Pepps")
pepps.down()

mary.up()
mary.goto(-500, -20)
mary.write("Mary")
mary.down()

for n in range(120):
    speed_pepps = random.randrange(1, 5)
    distance_pepps = random.randrange(1, 15)
    pepps.speed(speed_pepps)
    pepps.forward(distance_pepps)
    speed_mary = random.randrange(1, 5)
    distance_mary = random.randrange(1, 15)
    mary.speed(speed_mary)
    mary.forward(distance_mary)

wn.exitonclick()
