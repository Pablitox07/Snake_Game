import random
import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
start_position = [(0, 0), (-20, 0), (-40, 0)]
seg = []
score_points = 0
score_board = Turtle()
score_board.penup()
score_board.color('white')
score_board.goto(0, 280)
score_board.hideturtle()
score_board.write(f"Score: {score_points}", align='center', font=("Arial", 12, "normal"))
colores = ['white', 'blue', 'purple', 'green', 'pink', 'yellow', 'orange', 'gold', 'grey']

go_board = Turtle()
go_board.penup()
go_board.color('white')
go_board.hideturtle()


def turn_right():
    seg[0].right(90)


def turn_left():
    seg[0].left(90)


def game_over():
    global game_is_on
    if seg[0].xcor() < -290 or seg[0].xcor() > 290 or seg[0].ycor() < -290 or seg[0].ycor() > 290:
        go_board.write(f"GAME OVER\nSCORE: {score_points}", align='center', font=("Arial", 12, "normal"))
        game_is_on = False
    for each_part in range(1, len(seg)):
        if seg[0].distance(seg[each_part]) < 1:
            print(f"game over {score_points}")
            go_board.write(f"GAME OVER\nSCORE: {score_points}", align='center', font=("Arial", 12, "normal"))
            game_is_on = False


def follow_the_leader():
    for seg_num in range((len(seg)) - 1, 0, -1):
        new_x = seg[seg_num - 1].xcor()
        new_y = seg[seg_num - 1].ycor()
        seg[seg_num].goto(new_x, new_y)


def create_food_score_new_part():
    global score_points
    if seg[0].distance(food) < 18:
        food.goto(random.randint(-285, 285), random.randint(-285, 285))
        new_snake = Turtle('circle')
        new_snake.color(colores[random.randint(0,8)])
        new_snake.penup()
        score_points += 1
        score_board.clear()
        score_board.write(f"Score: {score_points}", align='center', font=("Arial", 12, "normal"))
        seg.append(new_snake)


score = 0
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "s")

screen.listen()

food = Turtle('circle')
food.color('green')
food.penup()
food.goto(random.randint(-285, 285), random.randint(-285, 285))

for position in start_position:
    new_part = Turtle('circle')
    new_part.color(colores[random.randint(0, 8)])
    new_part.penup()
    new_part.goto(position)
    seg.append(new_part)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    game_over()
    follow_the_leader()
    seg[0].forward(10)
    create_food_score_new_part()

screen.exitonclick()
