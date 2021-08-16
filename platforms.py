import turtle
DISTANCE = 20


class Platform:
    """Gives 5 squared turtles pointed to the North, requires x position"""
    def __init__(self, x_pos):
        self.block_bank = []
        for i in range(5):
            t = turtle.Turtle("square")
            t.penup()
            t.hideturtle()
            t.color("white")
            t.speed(0)
            t.goto(x_pos, 40-i*20)
            t.left(90)
            t.showturtle()
            self.block_bank.append(t)

    def move_up(self):
        for i in range(5):
            global DISTANCE
            self.block_bank[i].fd(DISTANCE)

    def move_down(self):
        for i in range(5):
            global DISTANCE
            self.block_bank[i].bk(DISTANCE)
