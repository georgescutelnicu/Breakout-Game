import random
import turtle
import time
from barrier import Barrier
from player import Player
from ball import Ball
from bricks import Bricks

# Turtle Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Breakout Game")
screen.tracer(0)

#Limits
barrier = Barrier()
barrier.draw_barrier()

#Player
player =  Player()
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

#Ball
ball= Ball()

#Bricks
bricks = []
x= -200
y= 200
for _ in range(5):
    x = -200
    for _ in range(9):
        brick=Bricks(x, y)
        bricks.append(brick)
        x += 50
    y -= 25

#Game functionality
is_game_on = True
while is_game_on:
    time.sleep(0.01)
    screen.update()
    ball.moove_ball()
    if ball.ycor() < -270:
        is_game_on = False
    if ball.ycor() > 262:
       ball.bounce_y()
    if ball.xcor() > 262 or ball.xcor() < -262:
        ball.bounce_x()
    if  ball.distance(player) < 33:
        ball.y_move = abs(random.randint(1,4))
    if bricks:
        for brick in bricks:
            if ball.distance(brick) < 20:
                brick.hideturtle()
                bricks.remove(brick)
                if abs(brick.ycor() - ball.ycor()) < 5 and abs(brick.xcor() - ball.xcor()) > 15: #4-8
                    ball.bounce_x()
                else:
                    ball.bounce_y()
    else:
        is_game_on = False


screen.exitonclick()