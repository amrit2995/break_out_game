from turtle import Turtle
import time


class ScoreBoard(Turtle):
    def __init__(self, high_score):
        super().__init__()
        self.high_score = high_score
        self.score = 0
        self.life = 3
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(380, 280)
        self.display_score()

    def display_score(self):
        self.write(f" High Score:{self.high_score}  Score:{self.score}   Life:{self.life}", font=("Courier", 10, "normal"), align='right')

    def score_update(self, level):
        add = {0: 20, 1: 40, 2: 60}
        self.clear()
        self.score += add[level]
        self.display_score()

    def life_update(self):
        self.clear()
        self.life -= 1
        self.display_score()


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 0)

    def notice(self, life, score):
        if life == 0:
            self.write(f"Game Over !!", font=("Courier", 40, "normal"), align='center')
            self.update_high_score(score, self.read_high_score())
            return False
        else:
            self.write(f"{life} lives left !!", font=("Courier", 40, "normal"), align='center')
        time.sleep(2)
        self.clear()
        return True

    def win_notice(self, life, score):
        self.write("You Won", font=("Courier", 40, "normal"), align='center')
        self.goto(0, -40)
        self.write(f"Final Score:{score}, Lives left:{life}", font=("Courier", 20, "normal"), align='center')
        self.update_high_score(score, self.read_high_score())

    def read_high_score(self):
        try:
            with open('high_score.txt', 'r') as file:
                high_score = file.read()
                return int(high_score)
        except FileNotFoundError:
            return 0

    def update_high_score(self, score, high_score):
        if score > high_score:
            with open('high_score.txt', 'w') as file:
                file.write(str(score))



