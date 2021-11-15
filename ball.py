from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1)
        self.color('red')
        self.shape('circle')
        self.penup()
        self.move_speed = 0.1
