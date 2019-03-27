import turtle

NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

radius = STARTING_RADIUS

#Draw circles
for count in range(NUM_CIRCLES):
    #draw circle
    turtle.circle(radius)

    #Get coordinates for next circle
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    #Calculate radius for next circle
    radius = radius + OFFSET

    #Posidtion turtle for next circle
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
