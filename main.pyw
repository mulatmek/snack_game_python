import time

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard


# global variable


def setting_keys(screen, snack):
    screen.onkey(snack.up, "Up")
    screen.onkey(snack.down, "Down")
    screen.onkey(snack.left, "Left")
    screen.onkey(snack.right, "Right")


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("my Snake Game")
        self.screen.tracer(0)
        self.BOARD_DETECT = 295

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.game_is_on = True

        # listen to events
        self.screen.listen()
        self.setting_keys()

    def setting_keys(self):
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def game_over(self):
        self.scoreboard.update_scoreboard("game_over")
        self.game_is_on = False

    def go(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            # collision with food
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.increase_score()
            # collision with wall
            if self.snake.head.xcor() > self.BOARD_DETECT or self.snake.head.xcor() < -self.BOARD_DETECT or self.snake.head.ycor() > self.BOARD_DETECT or self.snake.head.ycor() < -self.BOARD_DETECT:
                self.game_over()
            #colision with tail or any segment
            for seg in self.snake.segments[1:]:
                if self.snake.head.distance(seg)<10:
                    self.game_over()

        self.screen.exitonclick()


def main():
    snake_game = Game()
    snake_game.go()


if __name__ == '__main__':
    main()
