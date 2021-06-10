# Done by Carlos Amaral (2021/06/04)

from scores import ScoreBoard
from cars import Car
import time
from turtle import Screen, Turtle
from the_turtle import TheTurtle


screen = Screen()
screen.bgpic("road.png")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

the_turtle = TheTurtle()
cars = Car()
scores = ScoreBoard()

screen.onkeypress(fun=the_turtle.move, key="Up")

game_flow = True

while game_flow:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()


    # Detect collision with car
    for car in cars.cars:
        if car.distance(the_turtle) < 20:
            game_flow = False
            scores.game_over()


    # Detect successful crossing
    if the_turtle.turtle_finnish_line():
        the_turtle.reset()
        cars.level_up()
        scores.update()
 
    
    

screen.exitonclick()