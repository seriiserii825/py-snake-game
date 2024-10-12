from turtle import Turtle

from libs.screenSize import screenSize


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_name = "data.txt"
        self.high_score = 0
        self.getHighScore()
        monitors = screenSize()
        monitor_height = monitors[0].height - 120
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, monitor_height/2)
        self.updateScore()

    def getHighScore(self):
        with open(self.file_name) as file:
            self.high_score = int(file.read())

    def setHighScore(self):
        with open(self.file_name, mode="w") as file:
            file.write(str(self.high_score))

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.setHighScore()
        self.score = 0
        self.updateScore()

    def getScore(self):
        return self.score
