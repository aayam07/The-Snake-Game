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
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with Tail
    # if the head collides with any segment in the tail(any other segments), the trigger Game Over
    for segment in snake.segments[1:]:  # all the segments from index 1 (i.e the head segment at index 0 is excluded.)
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        # if segment != snake.head and snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()


screen.exitonclick()


# # Create Snake Body
# starting_x_positions = [0, -20, -40]  # x-coordinates
# # starting_positions = [(0, 0), (-20, 0), (-40, 0)] # this can be used in for loop and goto() alternatively
# segments = []
#
# for index in range(0, 3):
#     new_snake = Turtle(shape="square")
#     new_snake.color("white")
#     new_snake.penup()
#     new_snake.goto(x=starting_x_positions[index], y=0)
#     segments.append(new_snake)
#
# # Move the snake
# game_is_on = True
# while game_is_on:
#     # the screen will be updated only after all 3 segments move. It'll look like they are moving at once
#     screen.update()  # update should be called after each animation(movement of stuffs) when the tracer is off.
#     time.sleep(0.1)
#     # for segment in segments:
#     #     segment.forward(20)
#
#     for seg_num in range(len(segments) - 1, 0, -1):  # start, stop, step (0 is excluded)
#         new_x = segments[seg_num - 1].xcor()  # of second-last segment
#         new_y = segments[seg_num - 1].ycor()  # of second_last segment
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)
#     # segments[0].left(90)
