from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1, 5)
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(0, -260)

    def goleft(self):
        if self.xcor() >= -240:
            self.setx(self.xcor() - 20)

    def goright(self):
        if self.xcor() <= 240:
            self.setx(self.xcor() + 20)
