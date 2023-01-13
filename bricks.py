import turtle
from random import choice

COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'violet']

class Bricks(turtle.Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.shape('square')
        self.penup()
        self.goto(x, y)




