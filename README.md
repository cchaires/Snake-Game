# Snake Game

A simple snake game developed using the turtle graphics module in Python. The game involves controlling a snake to eat randomly generated food while avoiding collisions with the walls and the snake's own tail. 

## Files

### main.py

This is the main file that runs the game. It initializes the screen, snake, food, and scoreboard. It also sets up the event listeners for the arrow keys to control the snake's movement. The game runs in a while loop until the player collides with the wall or the snake's own tail.

### snake.py

This file contains the `Snake` class that defines the properties and behavior of the snake. The snake is represented as a list of turtle objects. The class has methods to move the snake, extend its length when it eats food, reset its position, and change its color.

### food.py

This file contains the `Food` class that defines the properties and behavior of the food. The food is represented as a turtle object that randomly generates its color and position on the screen. The class has a method to refresh the food's position when the snake eats it.

### scoreboard.py

This file contains the `Scoreboard` class that defines the properties and behavior of the scoreboard. The scoreboard keeps track of the player's score and high score. It updates the score whenever the snake eats food and resets the score and high score when the game ends.

## How to Play

1. Run the `main.py` file to start the game.
2. Control the snake's movement using the arrow keys.
3. Eat the food to increase your score.
4. Avoid colliding with the walls or the snake's own tail.
5. The game ends when the snake collides with the wall or its own tail.
