import turtle
import random

turtle.bgcolor('black')
turtle.speed(0)
turtle.hideturtle()

def main():
    buildings()
    windows()
    stars()



def buildings():
    turtle.penup()
    turtle.goto(-480, -100)
    turtle.pendown()
    turtle.color('gray')
    turtle.begin_fill()
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(190)
    turtle.right(90)
    turtle.forward(290)
    turtle.left(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(210)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(1000)
    turtle.end_fill()

def windows():
    turtle.penup()
    for i in range(6):
        turtle.goto(random.randint(-200,200),random.randint(-100,200))
        turtle.setheading(0)
        turtle.color('white')
        turtle.begin_fill()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.end_fill()

def stars():
    turtle.penup()
    for i in range(10):
        turtle.goto(random.randint(-400,400),random.randint(100,400))
        turtle.setheading(0)
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
main()
