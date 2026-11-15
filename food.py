from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.appear()

    def appear(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 320)
        self.goto(random_x, random_y)

    def reset(self):
        self.hideturtle()
        self.goto(1000, 1000)