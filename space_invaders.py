import turtle
import math
import random

# setup screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")

# Border
border_draw = turtle.Turtle()
border_draw.speed(0)
border_draw.pencolor("white")
border_draw.penup()
border_draw.setposition(-300, -300)
border_draw.pendown()
border_draw.pensize(3)

for side in range(4):
    border_draw.fd(600)
    border_draw.lt(90)
border_draw.hideturtle()

# Player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 10

# choose number of enemies
number_of_enemies = 5

# create empty list of enemies
enemies = []

# add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    enemy = turtle.Turtle()

# Invaders / Enemies

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemy_speed = 2

# Creating player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

# bullet state

# ready - ready to shoot
# fire - bullet is firing

bullet_state = "ready"


# move player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


# Fire bullet
def fire_bullet():
    global bullet_state  # declare bullet_state as global if its to be updated
    if bullet_state == "ready":
        bullet_state = "fire"

        # Move bullet above player ready
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


# check collision

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# keyboard bindings to listen

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main Game loop
while True:

    for enemy in enemies:
        # Move invaders
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move the invaders bounce off walls and down / Boundary checking
        if enemy.xcor() > 280:
            enemy_speed *= -1
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)

        if enemy.xcor() < -280:
            enemy_speed *= -1
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            
         # check collsion with enemy from bullet
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

    # Move bullet towards enemy
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # check bullet has reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

   

delay = input("Press enter to finish")
