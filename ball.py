from turtle import Turtle
import random
DISTANCE = 8

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fast")
        self.penup()
        self.color("white")
        self.start_position()

    def start_position(self):
        self.goto(0,0)
        self.setheading(45 + random.randint(0,0)*90)

    def move(self):
        self.fd(DISTANCE)
        print(self.heading())
        if self.position()[1] > 290 or self.position()[1] < -290:
            self.setheading(360 - self.heading())
