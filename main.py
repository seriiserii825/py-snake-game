import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40, 0)]
segments = []
game_is_on = True

for position in starting_positions:
    segment = Turtle("square")
    segment.color('white')
    segment.penup()
    segment.goto(position)
    segments.append(segment)


while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
