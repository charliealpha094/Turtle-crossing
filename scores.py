# Done by Carlos Amaral (2021/06/06)

from turtle import Turtle, left


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.level = 1
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

