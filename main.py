from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard, Border
from menu import Menu
import time

window = Screen()
window.bgcolor("black")
window.title("Snake Game")
window.setup(800, 800)
window.tracer(0)

menu = Menu()
window.update()

def start_game():
    window.onkey(None, "space")
    menu.clear_menu()
    window.update()

    snake = Snake()
    food = Food()
    score = ScoreBoard()
    border = Border()

    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.left, "Left")
    window.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        window.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.appear()
            snake.extend()
            score.inc_score()
            snake.inc_speed()

        if (snake.head.xcor() >= 370 or snake.head.xcor() <= -370 or
                snake.head.ycor() >= 340 or snake.head.ycor() <= -370):
            game_on = False

        for segment in snake.turtles[:-1]:
            if snake.head.distance(segment) < 10:
                game_on = False

    score.game_over()
    window.update()

window.listen()
window.onkey(start_game, "space")
window.exitonclick()