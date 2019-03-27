import turtle

NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 10

turtle.speed(ANIMATION_SPEED)

#Draw circle
for x in range (NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
