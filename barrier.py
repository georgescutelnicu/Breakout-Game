import turtle

class Barrier(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.barrier = turtle.Turtle()
        self.barrier.color("white")
        self.barrier.penup()
        self.barrier.goto(-270, 270)
        self.barrier.pendown()
        self.barrier.ht()

    def draw_barrier(self):
        for x in range(4):
            self.barrier.forward(540)
            self.barrier.right(90)

