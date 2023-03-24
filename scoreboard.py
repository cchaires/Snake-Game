from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("high_score_data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.scoreboard_text()

    def scoreboard_text(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.scoreboard_text()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_data.txt", mode="w") as w_file:
                w_file.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard_text()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", align=ALIGNMENT, font=FONT)
