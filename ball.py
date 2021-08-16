from turtle import Turtle
import random


class Ball:
    def __init__(self):
        t = Turtle("circle")
        t.speed("fast")
        t.penup()
        t.color("white")
        self.start_position()

    def start_position(self):
        self.goto(0,0)
        self.right(45)
        self.right(random.randint(0,3)*90)
        self.fd(100)

