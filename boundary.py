from turtle import Turtle


class DotedLine:
    def __init__(self):
        t = Turtle()
        t.hideturtle()
        t.color("white")
        t.speed(0)
        t.penup()
        t.goto(0, -400)
        t.pensize(10)
        t.left(90)

        while t.position()[1] < 420:
            t.pendown()
            t.fd(20)
            t.penup()
            t.fd(30)
