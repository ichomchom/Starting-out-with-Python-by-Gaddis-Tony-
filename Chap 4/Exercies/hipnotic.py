import turtle
turtle.speed(0)
for i in range (0,500, 20):

    turtle.setheading(90)
    turtle.forward(i + 10)
    turtle.setheading(180)
    turtle.forward(i + 10)
    turtle.setheading(270)
    turtle.forward(i + 20)
    turtle.setheading(0)
    turtle.forward(i + 20)
