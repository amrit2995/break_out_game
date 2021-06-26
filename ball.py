from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.ball_speed = 0.000009
        self.reset()

    def reset(self):
        self.goto(0, -230)
        self.setheading(random.randint(30, 150))

    def move(self):
        self.fd(10)

    def reflect_ball_x(self):
        direction = self.heading()
        if direction < 90:
            difference = direction
            self.setheading(180 - direction)
        elif direction < 180:
            difference = direction - 90
            self.setheading(90 - difference)
        elif direction < 270:
            difference = direction - 180
            self.setheading(360 - difference)
        else:
            difference = 360 - direction
            self.setheading(180 + difference)
        self.ball_speed *= 0.09

    def reflect_ball_y(self):
        direction = self.heading()
        self.setheading(360-direction)