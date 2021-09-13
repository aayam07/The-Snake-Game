from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # this can be used in for loop and goto()
# STARTING_X_POSITIONS = [0, -20, -40]  # x-coordinates
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Creates Snake Body

        self.segments = []  # attribute of the class(object)
        self.create_snake()  # calls the create_snake() method
        self.head = self.segments[0]  # head segment of the snake as attribute

    def create_snake(self):
        """Creates Snake Body."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the snake"""
        # print(self.segments[-1].position())
        self.add_segment(self.segments[-1].position())  # new segment is added to the same position as the last segment.

    def move(self):
        """Moves the snake."""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # new_heading = self.segments[0].heading() + 90  # this adds 90 to the heading it is currently facing
        # self.segments[0].setheading(new_heading)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # this adds 90 to the initial direction i.e east

    def left(self):
        # new_heading = self.segments[0].heading() + 90
        # self.segments[0].setheading(new_heading)
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # adds 180 to the initial direction (0+180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # means that it makes 270 degree angle with the initial direction i.e. with 0

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
