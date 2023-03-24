import time
import turtle
import snake
import food
import scoreboard


game_is_on = True
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)
screen.colormode(255)

snake = snake.Snake()
food = food.Food()
score_game = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    food.random_color()
    snake.random_color()
    snake.move_snake()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_game.increase_score()

    # Detect collisions with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_game.reset_score()
        snake.reset_snake_body()

    # Detect collisions with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_game.reset_score()
            snake.reset_snake_body()


screen.exitonclick()
