import turtle
turtle.speed(9)
for i in range(0,300,5):
    turtle.setheading(90)
    turtle.forward(i)
    turtle.setheading(180)
    turtle.forward(i)
    turtle.setheading(270)
    turtle.forward(i)
    turtle.setheading(0)
    turtle.forward(i)
