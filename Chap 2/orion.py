#This program draw the stars of the Orion constellation

import turtle

#Set the window size
turtle.setup(500, 600)

#setup the turtle
turtle.penup()
turtle.hideturtle()

#create name constant for star coordinates
LEFT_SH_X = -70
LEFT_SH_Y = 200

RIGHT_SH_X = 80
RIGHT_SH_Y = 180

LEFT_BELT_X = -40
LEFT_BELT_Y = -20

MID_BELT_X = 0
MID_BELT_Y = 0

RIGHT_BELT_X = 40
RIGHT_BELT_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

turtle.goto(LEFT_SH_X, LEFT_SH_Y) #go to left shoulder
turtle.dot()
turtle.goto(RIGHT_SH_X, RIGHT_SH_Y) #go to right shoulder
turtle.dot()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #go to left belt
turtle.dot()
turtle.goto(MID_BELT_X, MID_BELT_Y) #go to mid belt
turtle.dot()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #go to right belt
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #go to left knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #go to right knee
turtle.dot()

turtle.goto(LEFT_SH_X, LEFT_SH_Y) #go to left shoulder
turtle.write('Betegeuse')
turtle.goto(RIGHT_SH_X, RIGHT_SH_Y) #go to right shoulder
turtle.write('Meissa')
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #go to left belt
turtle.write('Alnitak')
turtle.goto(MID_BELT_X, MID_BELT_Y) #go to mid belt
turtle.write('Alnilam')
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #go to right belt
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #go to left knee
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #go to right knee
turtle.write('Rigel')

#Draw line
turtle.goto(LEFT_SH_X, LEFT_SH_Y)
turtle.pendown()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y)
turtle.penup()

turtle.goto(RIGHT_SH_X, RIGHT_SH_Y)
turtle.pendown()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y)
turtle.penup()

turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.pendown()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y)
turtle.penup()

turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.pendown()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y)
turtle.penup()

turtle.goto(LEFT_BELT_X, LEFT_BELT_Y)
turtle.pendown()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y)
turtle.penup()

#keep window open
turtle.done()
