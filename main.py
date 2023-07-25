from turtle import Screen
from snake import Snake
from food import Food, BonusFood
from scoreboard import ScoreBoard
import time

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600


class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.scoreboard = ScoreBoard()
        self.food = Food()
        self.bonus_food = BonusFood()
        self.bonus_food.hide_bonus()

        self.food.new_position(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.screen.listen()
        self.screen.onkey(fun=self.snake.move_up, key="Up")
        self.screen.onkey(fun=self.snake.move_down, key="Down")
        self.screen.onkey(fun=self.snake.move_right, key="Right")
        self.screen.onkey(fun=self.snake.move_left, key="Left")

    def start(self):
        bonus_food_timeout = 10  # Bonus food will appear for 10 seconds
        bonus_food_timer = time.time() + bonus_food_timeout

        while not self.scoreboard.is_game_over:
            self.screen.update()
            time.sleep(0.1)

            self.snake.move()

            # Check if snake ate food/bonus food
            if self.snake.head.distance(self.food) < 15:
                self.scoreboard.increase(1)
                self.snake.grow_snake()
                self.food.new_position(SCREEN_WIDTH, SCREEN_HEIGHT)
            elif self.snake.head.distance(self.bonus_food) < 15:
                self.scoreboard.increase(5)
                self.snake.grow_snake()
                self.bonus_food.new_position(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.bonus_food.hide_bonus()
                bonus_food_timer = time.time() + bonus_food_timeout

            # Check if bonus food timer expired and make the bonus food appear again
            if time.time() >= bonus_food_timer:
                self.bonus_food.new_position(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.bonus_food.show_bonus()
                bonus_food_timer = time.time() + bonus_food_timeout

            if (
                abs(self.snake.head.xcor()) > SCREEN_WIDTH / 2
                or abs(self.snake.head.ycor()) > SCREEN_HEIGHT / 2
                or self.snake.check_collision()
            ):
                self.scoreboard.game_over = True
                self.scoreboard.display_game_over()

        self.screen.exitonclick()


if __name__ == "__main__":
    game = SnakeGame()
    game.start()
