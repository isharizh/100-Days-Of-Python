from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def col(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()
