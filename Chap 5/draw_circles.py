import turtle

def main():
    turtle.hideturtle()
    circle(100, 0, 50, 'red')
    circle(-150, -100, 100, 'blue')
    circle(-200, 150, 75, 'green')

def circle(x, y, rad, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

main()           
