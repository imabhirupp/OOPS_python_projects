from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

# setting up the screen features
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)   # Stops the screen animation/transition

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# defining the keys for the snake movement
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()  # updates the screen animation/transition at our desired time
    time.sleep(0.1)  # delays the shift by the given time
    snake.move()

    # Checking the collision between food and snake head
    if snake.head.distance(food) < 15:            # checking the distance between the snake head and food is less than 15
        food.refresh()                            # refreshing the location of the food
        snake.extend()                            # increasing the snake size
        scoreboard.count()                        # increasing the score

    # collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()                          # resetting the scoreboard when snake collides with wall
        snake.reset()                               # resetting the snake

    # collision with body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()                      # resetting the snake when it collides with its own body



screen.exitonclick()