import turtle
X = 0
Y = -200
BASE_RAD = 100
MID_RAD = 60
HEAD_RAD = 40

turtle.hideturtle()

def main():
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()

def drawBase():
    turtle.penup()
    turtle.goto(X, Y)
    turtle.pendown()
    turtle.circle(BASE_RAD)

def drawMidSection():
    turtle.penup()
    turtle.goto(X, Y + 2 * BASE_RAD)
    turtle.pendown()
    turtle.circle(MID_RAD)
def drawArms():
    turtle.penup()
    turtle.goto(X + MID_RAD, Y + (2 * BASE_RAD) + MID_RAD )
    turtle.pendown()
    turtle.left(45)
    turtle.forward(70)
    L_HAND_X = turtle.xcor()
    L_HAND_Y = turtle.ycor()
    turtle.left(20)
    turtle.forward(20)
    turtle.goto(L_HAND_X, L_HAND_Y)
    turtle.setheading(0)
    turtle.right(20)
    turtle.forward(20)
    turtle.penup()
    turtle.goto(X - MID_RAD, Y + (2 * BASE_RAD) + MID_RAD )
    turtle.pendown()
    turtle.setheading(180)
    turtle.right(30)
    turtle.forward(35)
    turtle.right(25)
    turtle.forward(40)
    R_HAND_X = turtle.xcor()
    R_HAND_Y = turtle.ycor()
    turtle.left(20)
    turtle.forward(20)
    turtle.goto(R_HAND_X, R_HAND_Y)
    turtle.right(60)
    turtle.forward(20)
    
def drawHead():
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(X, Y + (2 * BASE_RAD) + (2 * MID_RAD))
    turtle.pendown()
    turtle.circle(HEAD_RAD)
    turtle.penup()
    turtle.goto(X - 15, Y + (2 * BASE_RAD) + (2 * MID_RAD) + 30)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(X - 15, Y + (2 * BASE_RAD) + (2 * MID_RAD) + 45)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(X + 15, Y + (2 * BASE_RAD) + (2 * MID_RAD) + 45)
    turtle.pendown()
    turtle.circle(5)

def drawHat():
    turtle.penup()
    turtle.goto(X - 50, Y + (2 * BASE_RAD) + (2 * MID_RAD) + 60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(100)
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(20)
    turtle.setheading(90)
    turtle.forward(40)
    turtle.setheading(180)
    turtle.forward(60)
    turtle.setheading(270)
    turtle.forward(40)
    turtle.setheading(180)
    turtle.forward(20)
    turtle.setheading(270)
    turtle.forward(20)
    turtle.end_fill()
    
main()
