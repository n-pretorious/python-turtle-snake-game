from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.is_game_over = False
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.color("white")
        self.update_score_display()

    def increase(self, points):
        self.score += points
        self.update_score_display()

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.penup()
        self.score_display.goto(0, 260)
        self.score_display.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    def display_game_over(self):
        self.is_game_over = True
        self.score_display.goto(0, 0)
        self.score_display.write(f"GAME OVER! \nFinal Score: {self.score}", align="center", font=("Courier", 24, "normal"))
