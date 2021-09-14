from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # 0 means off i.e. it turns of the animation tracing

snake = Snake()  # creates snake object(body)
food = Food()
scoreboard = Scoreboard()

screen.listen()  # to start listening for key strokes
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# moving the snake
game_is_on = True
while game_is_on:
    # refreshes the screen every 0.1 second
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        # scoreboard.clear()  # clears everything written by the turtle (i.e. previous score)
        # scoreboard.update_score()  # writes the increased score (i.e new score)
        food.refresh()
        snake.extend()  # adds new segment when snake hits the food

    # Detect Collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -298 or snake.head.ycor() > 285 or snake.head.ycor() < -300:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with Tail
    # if the head collides with any segment in the tail(any other segments), the trigger Game Over
    for segment in snake.segments[1:]:  # all the segments from index 1 (i.e the head segment at index 0 is excluded.)
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

        # if segment != snake.head and snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()


screen.exitonclick()
