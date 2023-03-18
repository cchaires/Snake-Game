import turtle
import random
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_CONSTANT = 20
SPEED_CONSTANT = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.draw_snake()
        self.head = self.snake_body[0]
        self.random_color()

    def draw_snake(self):
        for position in STARTING_POSITION:
            self.add_tail(position)

    def add_tail(self, position):
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        snake.speed("slowest")
        self.snake_body.append(snake)

    def extend(self):
        # add a new segment to snake
        self.add_tail(self.snake_body[-1].position())

    def move_snake(self):
        # moving the snake's head and tail, first tail, then head {self.snake_body[0].forward(20)}
        for s_tail in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[s_tail - 1].xcor()
            new_y = self.snake_body[s_tail - 1].ycor()
            self.snake_body[s_tail].goto(new_x, new_y)
        self.head.forward(MOVE_CONSTANT)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.head.color(r, g, b)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
