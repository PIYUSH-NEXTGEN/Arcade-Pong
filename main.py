from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong Arcade")
screen.tracer(0)

net = Turtle()
net.color("white")
net.penup()
net.hideturtle()
net.goto(0, 380)
net.setheading(-90)

for _ in range(38):
    net.forward(10)
    net.penup()
    net.forward(10)
    net.pendown()

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off top and bottom walls
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Right paddle missed
    if ball.xcor() > 390:
        ball.reset_position()
        score.left_point()

    # Left paddle missed
    if ball.xcor() < -390:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
