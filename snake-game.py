# Snake / Turtle game

import turtle
import time
import random


delay = 0.1

points = 0
high_score = 0

# screen setup
win = turtle.Screen()
win.title("Snake Game by Jaz")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0) # turns of screen updates

# snake 'turtle' head
head = turtle.Turtle()
head.speed(0) # animation speed of turtle module set to 0 fastest
head.shape("turtle")
# head.shapesize(2,2)
head.color("blue")
head.penup() # to ensure it does not draw
head.goto(0,0) # start in center of screen
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
# food.shapesize(1,1)
food.color("red")
food.penup()
food.goto(0,100)
# turtles/ snakes body growing parts
snake_parts = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score Points: 0 Highest Score: 0", align="center", font=("Roboto", 26, "normal"))

# Function to move

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Function to go up


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings


win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")


# main game loop
while True:
    win.update()

    # check for border collision
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1) # pauses the game
        head.goto(0,0) # set snake to center for restart
        head.direction = "stop" # stops game

    # remove / hide snake new parts
        for part in snake_parts:
            part.goto(1000,1000) # moves old segments way off screen

        # clear the parts
        snake_parts.clear()

        # resets points when died and hit border
        points = 0

        # reset delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(points, high_score), align="center", font=("Roboto", 26, "normal"))

        # check for collision with food
    if head.distance(food) < 20:
        # move food to random location in window
        x = random.randint(-290, 290)
        y = random.randint(-290,290)
        food.goto(x,y)

    # add new food part
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("turtle")
        new_part.color("black")
        new_part.penup()
        snake_parts.append(new_part)

        # shorten the delay
        delay -= 0.001

        # increase score points
        points += 5

        if points > high_score:
            high_score = points

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(points,high_score), align="center", font=("Roboto", 26, "normal"))

    # move end parts first in reverse - only done when move than 1 snake part
    for index in range(len(snake_parts)-1, 0, -1):
        x = snake_parts[index-1].xcor()
        y = snake_parts[index-1].ycor()
        snake_parts[index].goto(x,y)

    # Move snake part 0 to where the head is
    # - checks is there a length over 0, if yes then the first snake part will move to 0,0

    if len(snake_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        snake_parts[0].goto(x,y)

    move()

    # check for head collision with snake body part
    for part in snake_parts:
        if part.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for part in snake_parts:
                part.goto(1000, 1000)  # moves old segments way off screen

            # clears the parts
            snake_parts.clear()

            points = 0 #reset points

            delay = 0.1
    time.sleep(delay)

win.mainloop()
