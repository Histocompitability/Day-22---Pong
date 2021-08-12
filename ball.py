from turtle import Turtle
import random

class Ball:
    def __init__(self):
        t = Turtle("circle")
        t.speed(0)
        t.penup()
        t.color("white")
        self.start_position()

    def start_position(self):
        global t
        t.goto(0.0)
        t.right(45)
        t.right(random.randint(0,3)*90)
