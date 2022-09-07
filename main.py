import time
from snack import Snack
from turtle import Screen
from food import Food


def setting_keys(screen, snack):
    screen.onkey(snack.up, "Up")
    screen.onkey(snack.down, "Down")
    screen.onkey(snack.left, "Left")
    screen.onkey(snack.right, "Right")


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("my Snake Game")
    screen.tracer(0)

    snack = Snack()
    food = Food()

    # listen to events
    screen.listen()
    setting_keys(screen, snack)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snack.move()
        if snack.head.distance(food) < 15:
            food.refresh()
        # collision with food

    screen.exitonclick()


if __name__ == '__main__':
    main()
