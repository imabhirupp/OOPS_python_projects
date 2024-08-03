from turtle import Turtle


class Ball(Turtle):
    # Giving shape to the ball
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 0.7, stretch_wid=0.7)
        self.color("white")
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1                # ball speed set to 0.1

    # Creating the ball movements
    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_move  # creating a x-axis point within the used screen size for the ball
        new_y = self.ycor() + self.y_move  # creating a y-axis point within the used screen size for the ball
        self.goto(new_x, new_y)

# Creating the bouncing movement of the ball
    def y_bounce(self):
        self.y_move *= -1       # ball movement is (x++,y++) where x and y starts from 0. So in order to bounce it back we just need to change the y coordinate since x will be increasing with the same amount just that y will start decreasing with the same amount after hitting the wall (print out new_x and new_y variables in order to understand properly)

    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9           # after every collision ball speed increases by 0.9 times

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1            # resets the ball speed when either of the paddle misses
        self.x_bounce()
