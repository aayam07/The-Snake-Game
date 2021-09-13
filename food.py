from turtle import Turtle
import random

FOOD_COLOR = "yellow"
FOOD_SHAPE = "circle"


# Inheritance. Food is the child class and Turtle is the parent(super) class.
class Food(Turtle):
    # to represent all the thing belonging to the object inside the class of the object, we use self
    def __init__(self):
        super().__init__()  # initializes everything that the super class(Turtle) can do.
        # self.food = Turtle()  # using inheritance instead of this way.
        self.shape(FOOD_SHAPE)  # by doing this we don't need to call these using object of child class.
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 circle (i.e multiplies original len & width by no.)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)
