from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.initial_score = -1
        self.speed(0)
        self.hideturtle()
        self.goto(position)
        self.color("white")

    def update_score(self):
        """prints a new score and adds 1 to it. After first called time prints 0"""
        self.clear()
        self.initial_score += 1
        self.write(self.initial_score, False, "Center", ("Courier", 30, "bold"))


class Game_Over_Message(Score):
    def __init__(self):
        super().__init__(position=(0, 0))
        self.initial_score = "Game Over"
        self.write(self.initial_score, False, "Center", ("Courier", 50, "bold"))
