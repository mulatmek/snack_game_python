from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard("update")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard("update")

    def update_scoreboard(self,update):
        if update=="update":
            self.write(f"your score is : {self.score}", align=ALIGNMENT, font=FONT)
        else:
            self.penup()
            self.hideturtle()
            self.goto(0, 0)
            self.write(f"GAME_OVER :( ", align=ALIGNMENT, font=FONT)

