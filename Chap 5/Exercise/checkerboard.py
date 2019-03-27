import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(-200,200)
turtle.speed(0)

def main():
    for i in range(5):
        if (i % 2 == 0):
            line(0, 5)
        else:
            line(1, 6)    
            
def square():
    turtle.pendown()
    for i in range(4):
        turtle.forward(60)
        turtle.right(90)
    turtle.setheading(0)
    turtle.forward(60)

def line(x, y):
    for i in range(x, y):
        if( i % 2) == 0:
            turtle.begin_fill()
            square()
            turtle.end_fill()
        else:
            square()
    turtle.backward(300)
    turtle.setheading(270)
    turtle.forward(60)
    turtle.setheading(0)
    
main()
