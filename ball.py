from turtle import Turtle
import random

# TODO make ball and let it bounce
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -400)
        self.setheading(random.randint(30, 150))

    def move(self):
        self.forward(8)

    def bounce(self):
        self.setheading(180 - self.heading())

    def bounce_vert(self, angle):
        self.setheading(self.heading() * angle)

    def ball_reset(self):
        self.goto(0, 0)
        self.setheading(random.randint(30, 150))