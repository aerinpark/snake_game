from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

class SnakeGame():
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.game_on = True
        self.set_game()
        self.start_game()

    def set_game(self):
        self.screen.clear()

        self.screen.tracer(0)
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(self.snake.move_up, "Up")
        self.screen.onkey(self.snake.move_down, "Down")
        self.screen.onkey(self.snake.move_left, "Left")
        self.screen.onkey(self.snake.move_right, "Right")

    def start_game(self):
        while self.game_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            if self.snake.head.distance(self.food) < 2:
                self.food.set_location()
                self.scoreboard.score_up()
                self.snake.grow()
            
            if self.snake.wall_collision():
                self.game_on = False
                self.scoreboard.game_over()
            
            for body in self.snake.body_parts[1:]:
                if self.snake.head.distance(body) < 10:
                    self.game_on = False
                    self.scoreboard.game_over()
            
        self.screen.exitonclick()