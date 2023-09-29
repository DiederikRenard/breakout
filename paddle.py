from turtle import Turtle


# TODO make paddle and move paddle horizontally


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.goto(0, -450)
        self.shape("circle")
        self.width(30)
        self.shapesize(1, 10, 10)
        self.setheading(0)

    def move_left(self):
        self.backward(50)


    def move_right(self):
        self.forward(50)