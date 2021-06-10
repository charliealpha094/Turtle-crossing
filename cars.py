# Done by Carlos Amaral (2021/06/05)

from hashlib import new
from turtle import Turtle
import random
COLORS = ["Red", "Orange", "Yellow", "Green", "Blue", 
        "Indigo", "Violet"]



class Car:
    def __init__(self):
        self.cars = []
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)


    def move_car(self):
        # Go through our list of cars
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10

   