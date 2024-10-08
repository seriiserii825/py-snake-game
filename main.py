from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

squares = []

for index in range(0, 4):
    tim = Turtle("square")
    x = index * -20
    tim.setpos(x, 0)
    tim.color('white')
    squares.append(tim)



screen.exitonclick()
