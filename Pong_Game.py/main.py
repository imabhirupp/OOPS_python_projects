from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

ball = Ball()
screen = Screen()
scoreboard = Scoreboard()

# Creating the screen
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Abhirup's Pong Game")

# Stopping the animation
screen.tracer(0)

# Creating two paddles and allocating their positions by calling the Paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Allocating the keys for moving both the paddles
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

# Updating the screen in order to show the screen after the animation
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)         # to increase the ball speed after each collision
    ball.move()

    # collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Bounces when hits the wall
        ball.y_bounce()

    # collision with both the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # right paddles misses, left paddle player A gets a point
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_scoreboard()

    # left paddle misses, right paddle player B gets a point
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_scoreboard()

    # On reaching a score of 5 game ends
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()