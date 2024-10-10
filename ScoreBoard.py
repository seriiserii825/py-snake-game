from turtle import Turtle

from libs.screenSize import screenSize


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        monitors = screenSize()
        monitor_height = monitors[0].height - 120
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, monitor_height/2)
        self.updateScore()

    def updateScore(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

