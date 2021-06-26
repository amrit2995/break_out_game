from turtle import Turtle
direction = {'right': 0, 'left': 180}


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.color('white')
        self.reset()

    def left(self):
        if self.xcor() > -320:
            self.bk(40)

    def right(self):
        if self.xcor() < 320:
            self.fd(40)

    def reset(self):
        self.goto(0, -250)

