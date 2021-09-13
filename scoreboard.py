from turtle import Turtle
# Global Constants
TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = "Courier"
FONT_SIZE = 12
FONT_STYLE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
