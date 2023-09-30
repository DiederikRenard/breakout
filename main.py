from tkinter import *
from turtle import *
import time
import random
from paddle import Paddle
from ball import Ball
from score import GameOver, Lives, Win

COLOURS = ["blue", "green", "red", "purple", "orange", "yellow"]
# Breakout
level = 1


# TODO make objects to hit
class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLOURS))
        self.shapesize(1, 4, 5)


# TODO increase difficulty after completion


game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.screensize(600, 600)
screen.tracer(0)

score = 0
lives = Lives()

block_list = []
paddle = Paddle()
ball = Ball()
for i in range(-5, 6):
    for n in range (0, 5):
        cor_x = i * 110
        cor_y = (n * 50) + 150
        block = Blocks()
        block.goto(cor_x, cor_y)
        block_list.append(block)


if __name__ == "__main__":
    while game_is_on:
        ball.move()
        listen()
        onkeypress(fun=paddle.move_left, key="Left")
        onkeypress(fun=paddle.move_right, key="Right")
        if ball.xcor() <= -610 or ball.xcor() >= 610:
            ball.bounce()
        if ball.ycor() >= 510:
            ball.bounce_vert(-1)
        if ball.ycor() < -450 and ball.distance(paddle) < 90:
            if ball.xcor()+10 < paddle.xcor() and ball.heading() > 275:
                ball.bounce_vert(-0.8)
            elif ball.xcor()-10 > paddle.xcor() and 180 < ball.heading() < 275:
                ball.bounce_vert(-1.2)
            else:
                ball.bounce_vert(-1)
        if ball.ycor() < -600:
            ball.goto(0, -200)
            ball.setheading(random.randint(30, 150))
            lives.sub_score()
        for block in block_list:
            if ball.distance(block) < 50:
                ball.bounce_vert(-1)
                block.goto(1000, 1000)
                score += 1
        if lives.lives == 0:
            game_is_on = False
            GameOver()

        if score >= len(block_list):
            game_is_on = False
            Win()




        screen.update()
        time.sleep(0.00000000000000005)
    exitonclick()

