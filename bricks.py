from turtle import Turtle

brick_color = ['green', 'blue', 'red']


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.level = None
        self.shapesize(stretch_wid=1, stretch_len=3, outline=4)
        self.color('white')
        self.penup()


class Bricks:
    bricks = []

    def __init__(self):
        for y in range(100, 270, 25):
            for x in range(-400, 400, 65):
                col_index = 0
                brick = Brick()
                self.bricks.append(brick)
                brick.goto(x, y)
                if y < 150:
                    brick.color(brick_color[0])
                    brick.level = 0
                elif y < 220:
                    brick.color(brick_color[1])
                    brick.level = 1
                else:
                    brick.color(brick_color[2])
                    brick.level = 2

    def ball_hit_brick(self, brick):
        self.bricks.remove(brick)
        brick.hideturtle()
