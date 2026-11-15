from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 355)
        self.hideturtle()
        self.update_scoreboard()

    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_highscore(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.highscore))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=("Courier", 20, "normal"))

    def inc_score(self):
        self.score += 10
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, 0)
        self.write(f"Game Over\nFinal Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        self.clear()
        self.goto(1000, 1000)

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-370, 340)
        self.pendown()
        self.pencolor("white")
        self.pensize(3)
        self.hideturtle()
        self.forward(740)
        self.right(90)
        self.forward(710)
        self.right(90)
        self.forward(740)
        self.right(90)
        self.forward(710)
        self.right(90)

    def reset(self):
        self.clear()