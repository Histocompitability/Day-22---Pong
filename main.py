from turtle import Screen
from score import Score, Game_Over_Message
from boundary import DotedLine
from platforms import Platform
from ball import Ball
import time


def left_up_dash():
    for _ in range (5):
        platform_player_left.move_up()
    screen.update()


def left_down_dash():
    for _ in range (5):
        platform_player_left.move_down()
    screen.update()


def right_up_dash():
    for _ in range (5):
        platform_player_right.move_up()
    screen.update()


def right_down_dash():
    for _ in range (5):
        platform_player_right.move_down()
    screen.update()


def left_up():
    platform_player_left.move_up()
    screen.update()


def left_down():
    platform_player_left.move_down()
    screen.update()


def right_up():
    platform_player_right.move_up()
    screen.update()


def right_down():
    platform_player_right.move_down()
    screen.update()


def game_is_on_func():
    global game_is_on
    game_is_on = False
    Game_Over_Message()

def ball_bounce_of_platform(direction):
    global ball
    if direction < 180:
        ball.setheading(180 - direction)
        ball.move()
        ball.move()
    elif direction < 360:

        ball.setheading(540 - direction)
        ball.move()
        ball.move()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

score_player_left = Score((-100, 250))
score_player_right = Score((100, 250))
score_player_left.update_score()
score_player_right.update_score()

doted_line_in_the_middle = DotedLine()
screen.tracer(0)
platform_player_left = Platform(-380)
platform_player_right = Platform(380)

screen.update()
screen.listen()
screen.onkeypress(left_up, "q")
screen.onkeypress(left_down, "a")
screen.onkeypress(right_up, "]")
screen.onkeypress(right_down, "'")
screen.onkeypress(left_up_dash, "w")
screen.onkeypress(left_down_dash, "s")
screen.onkeypress(right_up_dash, "[")
screen.onkeypress(right_down_dash, ";")
screen.onkeypress(game_is_on_func, "space")

ball = Ball()
game_is_on = True
speed_of_the_ball = 0.04
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(speed_of_the_ball)
    for i in range(0, 5):
        if ((ball.distance(platform_player_left.block_bank[i]) < 19 or
        ball.distance(platform_player_right.block_bank[i]) < 19) and
        (ball.position()[0] < 382 or ball.position()[0] > -380)):
            ball_bounce_of_platform(ball.heading())
    if ball.position()[0] > 400:
        score_player_left.update_score()
        ball.start_position()
        speed_of_the_ball /= 1.4
    elif ball.position()[0] < -400:
        score_player_right.update_score()
        ball.start_position()
        speed_of_the_ball /= 1.4

screen.exitonclick()
