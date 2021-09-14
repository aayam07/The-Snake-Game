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
        with open("data.txt") as high_score_file:  # to track record of the high score
            self.high_score = int(high_score_file.read())  # reads the content of the file as string, so converting to int()
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score_file:
                high_score_file.write(str(self.high_score))  # f"{self.high_score}"
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
