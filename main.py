from tkinter import *
from turtle import *
import time
from paddle import Paddle
import random


# Breakout

# TODO make ball and let it bounce
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(30, 150))

    def move(self):
        self.forward(9)

    def bounce(self):
        self.setheading(180 - self.heading())

    def bounce_vert(self, angle):
        self.setheading(self.heading() * angle)

    def ball_reset(self):
        self.goto(0, 0)
        self.setheading(random.randint(30, 150))

# TODO make objects to hit

# TODO objects disappear after hit

# TODO increase difficulty after completion


game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.screensize(600, 600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
if __name__ == "__main__":
    while game_is_on:
        ball.move()
        listen()
        onkey(paddle.move_left, "Left")
        onkey(paddle.move_right, "Right")
        if ball.xcor() <= -600 or ball.xcor() >= 600:
            print(ball.xcor(), ball.ycor())
            ball.bounce()
        if ball.ycor() >= 500:
            ball.bounce_vert(-1)
        if ball.ycor() < -450 and ball.distance(paddle) < 70:
            if ball.xcor()+10 < paddle.xcor() and ball.heading() > 275:
                ball.bounce_vert(-0.8)
            elif ball.xcor()-10 > paddle.xcor() and 180 < ball.heading() < 275:
                ball.bounce_vert(-1.2)
            else:
                ball.bounce_vert(-1)
        if ball.ycor() < -600:
            ball.ball_reset()
        screen.update()
        time.sleep(0.0000005)
    exitonclick()

