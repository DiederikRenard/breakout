from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.write("Game Over!!", align="center", font=("Ariel", 60, "bold"))


class Win(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.write("You win!!", align="center", font=("Ariel", 60, "bold"))



class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=450)
        self.write(f"Lives: {self.lives}", align="center", font=("Ariel", 20, "bold"))

    def sub_score(self):
        self.clear()
        self.lives -= 1
        self.write(f"Lives: {self.lives}", align="center", font=("Ariel", 20, "bold"))