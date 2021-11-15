from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(300, 240)
        self.write(self.score, align="center", font=("courier", 30, "normal"))

    def point(self):
        self.score += 7
        self.update_scoreboard()