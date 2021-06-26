from bricks import Bricks
from player_bar import Player
from ball import Ball
from scoreboard import ScoreBoard, Game

######################################

from turtle import Turtle, Screen
import time

window = Screen()
window.setup(width=800, height=600)
window.bgcolor('black')
window.tracer(0)
window.title("Breakout")
player = Player()
ball = Ball()

window.listen()
window.onkey(player.left, 'Left')
window.onkey(player.right, 'Right')
wall = Bricks()
game = Game()
high_score = game.read_high_score()
scoreboard = ScoreBoard(high_score)
game_on = True

while game_on:
    window.update()
    time.sleep(ball.ball_speed)
    ball.move()
    game.read_high_score()
    if len(wall.bricks) == 0:
        game_on = game.win_notice(scoreboard.life, scoreboard.score)
    for brick in wall.bricks:
        if brick.distance(ball) < 30 and (brick.ycor()-10 < ball.xcor() or brick.ycor()+10 > ball.xcor()):
            wall.ball_hit_brick(brick)
            ball.reflect_ball_y()
            scoreboard.score_update(brick.level)
        elif brick.distance(ball) < 30 and (brick.xcor()-30 < ball.xcor() or brick.xcor()+30 < ball.xcor()):
            wall.ball_hit_brick(brick)
            ball.reflect_ball_x()
            scoreboard.score_update(brick.level)
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.reflect_ball_x()

    if ball.ycor() > 280:
        ball.reflect_ball_y()

    if ball.ycor() < -280:
        scoreboard.life_update()
        game_on = game.notice(scoreboard.life, scoreboard.score)
        ball.reset()
        player.reset()


    if ball.ycor() < -230 and ball.distance(player) < 80:
        ball.reflect_ball_y()

    if ball.ycor() > 280:
        ball.reflect_ball_y()
    elif ball.ycor() < -280:
        pass


window.exitonclick()
