import time
from turtle import Screen

from Snake import Snake
from libs.screenSize import screenSize

monitor_width = screenSize().width
print(f"monitor_width: {monitor_width}")

screen = Screen()
screen.setup(width=monitor_width - 40, height=600, startx=20, starty=20)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
