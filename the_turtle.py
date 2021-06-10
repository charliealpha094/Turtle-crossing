# Done by Carlos Amaral (2021/06/05)

from turtle import Turtle

START_POSITION = (0, -270)

class TheTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("blue")
        self.reset()

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(START_POSITION)

    def turtle_finnish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False 