from turtle import Screen
from score import Score
from boundary import DotedLine
from platforms import Platform
from ball import Ball


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

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

#score - template
score_player_left = Score((-100, 250))
score_player_right = Score((100, 250))
score_player_left.update_score()
score_player_right.update_score()

doted_line_in_the_middle = DotedLine()
platform_player_left = Platform(-380)
platform_player_right = Platform(380)
# screen.tracer(0)


screen.listen()
screen.onkeypress(left_up, "q")
screen.onkeypress(left_down, "a")
screen.onkeypress(right_up, "]")
screen.onkeypress(right_down, "'")

ball = Ball()

screen.exitonclick()
