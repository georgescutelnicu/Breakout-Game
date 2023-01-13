import random
import turtle

class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.turtlesize(0.6)
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.goto(-150, -150)


    def moove_ball(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
