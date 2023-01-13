import turtle

class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(0.8,4)
        self.sety(-270)

    def move_right(self):
        x = self.xcor() + 20
        if self.xcor() <= 200:
            self.goto(x, self.ycor())

    def move_left(self):
        x = self.xcor() - 20
        if self.xcor() >= -200:
            self.goto(x, self.ycor())

