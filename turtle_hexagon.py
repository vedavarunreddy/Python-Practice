from turtle import *

# turtle_hexagon = Turtle()
# turtle_hexagon.shape("turtle")

def turtle_hexagon_shape():
    turtle_hexagon = Turtle()
    turtle_hexagon.shape("turtle")
    HEXAGON_ANGLE = 60 
    turtle_hexagon.color('orange')
    turtle_hexagon.begin_fill()
    for _ in range(6):
        turtle_hexagon.speed(2)
        turtle_hexagon.forward(80)
        turtle_hexagon.right(HEXAGON_ANGLE)
    turtle_hexagon.end_fill()
    exitonclick()

turtle_hexagon_shape()
    