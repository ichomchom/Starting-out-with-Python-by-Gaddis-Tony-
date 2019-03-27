#Hit the target game
import turtle

#name constatns
SCREEN_WIDTH = 600 #screen width
SCREEN_HEIGHT = 600 #SCREEN HEIGHT
TARGET_LLEFT_X = 100 #TARGET'S LOWER LEFT
TARGET_LLEFT_Y = 250 #Target's lower left y
TARGET_WIDTH = 25 #width of the target
FORCE_FACTOR = 30 #arbitrary force factor
PROJECTILE_SPEED = 1 #projectile's animation speed
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

#set up the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#Draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

#Center the turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#Get the angle an force from the user
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

#Calculate the distance
distance = force * FORCE_FACTOR

#Set heading
turtle.setheading(angle)

#Launch the projectile
turtle.pendown()
turtle.forward(distance)

#Check if hit the target
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('TARGET HIT!')
else:
        
        if (turtle.xcor() < TARGET_LLEFT_X):
                print('Try smaller angle')
        else: # (turtle.xcor() > TARGET_LLEFT_X):
                print('Try larger angle')
                
        if (turtle.ycor() < TARGET_LLEFT_Y):
                print('Use more force')
        else: # (turtle.ycor() >TARGET_LLEFT_Y):
                print('Use less force')

