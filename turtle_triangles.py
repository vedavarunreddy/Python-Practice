from turtle import *

turtle_triangle = Turtle()
turtle_triangle.shape("turtle")

def draw_triangle():
    turtle_triangle.color("orange")
    turtle_triangle.begin_fill
    ANGLE = 120
    for _ in range(3):
        turtle_triangle.forward(150)
        turtle_triangle.left(ANGLE)  
    turtle_triangle.end_fill()

# for i in range(3):
#     turtle_triangle = Turtle()
#     turtle_triangle.shape("turtle")
#     turtle_triangle.color("orange")
draw_triangle()
    