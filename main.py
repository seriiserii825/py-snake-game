import time
from turtle import Screen

from Snake import Snake
from libs.screenSize import screenSize

monitors = screenSize()
if len(monitors) == 2:
    startx = monitors[1].x
else:
    startx = monitors[0].x

monitor_width = monitors[0].width

print(f"monitor_width: {monitor_width}")

screen = Screen()
screen.setup(width=monitor_width - 40, height=600, startx=startx, starty=20)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
