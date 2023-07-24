from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()

screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

game_is_over = False
while not game_is_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
