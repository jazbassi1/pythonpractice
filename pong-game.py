# Pong game

import turtle
import os


win = turtle.Screen()
win.title("Pong Game - Jaz")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
sound = os.system("")

# Scores
score_1 = 0
score_2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()

paddle_1.speed(0)  # sets animation speed to max
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)


# Paddle 2
paddle_2 = turtle.Turtle()

paddle_2.speed(0)  # sets animation speed to max
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


# Ball
ball = turtle.Turtle()

ball.speed(0) # issue - ball speed is set to 0 lowest speed for turtle but still goes very fast
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed()
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Roboto", 24, "normal"))



# Function


def paddle_1_up():
    y = paddle_1.ycor() # returns y coordinate of paddle 1
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor() # returns y coordinate of paddle 1
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor() # returns y coordinate of paddle 1
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor() # returns y coordinate of paddle 1
    y -= 20
    paddle_2.sety(y)

# keyboard binding - listens for keyboard response from users


win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")


# main game loop - causes issues below

while True:
    win.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check for ball restrictions

    # top and bottom borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # left and right borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Roboto", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Roboto", 24, "normal"))

    # Paddle and Ball bounces

    if ball.xcor() < -340 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        os.system("")

    elif ball.xcor() > 340 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

