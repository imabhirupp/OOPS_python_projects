import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_turtle.up,"w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()

    # detect collision between car and player turtle
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            scoreboard.game_over()                       # GAME OVER PROMPT
            game_is_on = False


    # if reach finish line then start again from the starting point
    if player_turtle.finish_line():
        player_turtle.goto_start()
        car_manager.level_up()                           # Leveling up each time turtle reaches finish line
        scoreboard.increase_level()

screen.exitonclick()