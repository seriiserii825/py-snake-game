from turtle import Turtle

from libs.screenSize import screenSize


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        monitors = screenSize()
        monitor_height = monitors[0].height - 120
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, monitor_height/2)
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.updateScore()

    def getScore(self):
        return self.score
