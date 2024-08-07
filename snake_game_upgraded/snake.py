
from turtle import Turtle


POSITION = [(0,0), (-20,0), (-40,0)]     # Creating constant value
FORWARD = 20                            # Creating constant value
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]    # creating an attribute to set the head to the first value in the segments

# creating the snake and defining it's features
    def create_snake(self):
        for positions in POSITION:
            self.add_segment(positions)

    # resetting the snake segments and creating a new snake each time the game overs
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, positions):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    # increasing the snake size i.e. adding new segments to the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())        # adding segments to the last position in the list


    # defining the movement of the snake i.e. the 3 different turtle pieces
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # starting to take input in the reverse order
            x_new = self.segments[seg_num - 1].xcor()         # getting the x-coordinate of the 2nd last input and storing it
            y_new = self.segments[seg_num - 1].ycor()         # getting the y-coordinate of the 2nd last input and storing it
            self.segments[seg_num].goto(x_new, y_new)         # sending the last input to the 2nd last's posi and 2nd last input to the third last's posi
        self.head.forward(FORWARD)

# checking the movement of the snake head according to the key pressed
    def up(self):
        if self.head.heading() != DOWN:                      # Checking and making sure that the direction of the head is not pointing downward else it won't be allowed to move upward according the rule of the game
            self.head.setheading(UP)                         # rotating the direction of the first segments i.e. setting the heading by 90 degrees

    def down(self):
        if self.head.heading() != UP:                        # Checking and making sure that the direction of the head is not pointing upward else it won't be allowed to move downward according the rule of the game
            self.head.setheading(DOWN)                       # rotating the direction of the first segments i.e. setting the heading by 270 degrees

    def left(self):
        if self.head.heading() != RIGHT:                     #  Checking and making sure that the direction of the head is not pointing right else it won't be allowed to left upward according the rule of the game
            self.head.setheading(LEFT)                       # rotating the direction of the first segments i.e. setting the heading by 180 degrees

    def right(self):
        if self.head.heading() != LEFT:                      # Checking and making sure that the direction of the head is not pointing left else it won't be allowed to move right according the rule of the game
            self.head.setheading(RIGHT)                      # rotating the direction of the first segments i.e. setting the heading by 0 degrees


