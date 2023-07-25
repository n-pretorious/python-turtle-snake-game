from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self._init_food()

    def _init_food(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fast")

    def new_position(self, screen_width, screen_height):
        x_cord = randint(-screen_width // 2 + 20, screen_width // 2 - 20)
        y_cord = randint(-screen_height // 2 + 20, screen_height // 2 - 20)

        self.goto(x_cord, y_cord)


class BonusFood(Food):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")

    def show_bonus(self):
        self.showturtle()

    def hide_bonus(self):
        self.hideturtle()
