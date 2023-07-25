from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MOVE_DISTANCE = 20


class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.food.new_position(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.screen.listen()
        self.screen.onkey(fun=self.snake.move_up, key="Up")
        self.screen.onkey(fun=self.snake.move_down, key="Down")
        self.screen.onkey(fun=self.snake.move_right, key="Right")
        self.screen.onkey(fun=self.snake.move_left, key="Left")

        self.game_is_over = False

    def start(self):
        while not self.game_is_over:
            self.screen.update()
            time.sleep(0.1)

            self.snake.move()

            if self.snake.head.distance(self.food) < 15:
                self.snake.grow_snake()
                self.food.new_position(SCREEN_WIDTH, SCREEN_HEIGHT)

            if (
                abs(self.snake.head.xcor()) > SCREEN_WIDTH / 2
                or abs(self.snake.head.ycor()) > SCREEN_HEIGHT / 2
                or self.snake.check_collision()
            ):
                self.game_is_over = True
                self.display_game_over()

        self.screen.exitonclick()

    @staticmethod
    def display_game_over():
        game_over_text = Turtle()
        game_over_text.color("white")
        game_over_text.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


if __name__ == "__main__":
    game = SnakeGame()
    game.start()
