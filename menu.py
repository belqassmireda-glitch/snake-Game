from turtle import Turtle

class Menu(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.draw_menu()

    def draw_menu(self):
        self.goto(0, 100)
        self.write("SNAKE GAME", align="center", font=("Courier", 40, "bold"))
        self.goto(0, 0)
        self.write("Press SPACE to Start", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -60)
        self.write("Use Arrow Keys to Move", align="center", font=("Courier", 18, "normal"))

    def clear_menu(self):
        self.clear()