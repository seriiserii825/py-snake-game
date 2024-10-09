import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, monitor_width, monitor_height): 
        super().__init__() 
        self.monitor_width = monitor_width
        self.monitor_height = monitor_height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('orange')
        self.speed('fastest')
        x = monitor_width / 2
        x = round(x) - 40
        y = monitor_width / 2
        y = round(y) - 40
        random_x = random.randint(-x, x)
        print(f"random_x: {random_x}")
        random_y = random.randint(-y, y)
        print(f"random_y: {random_y}")
        self.goto(random_x,random_y)
