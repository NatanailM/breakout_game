from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.shapesize(1, 10)
        self.penup()
        self.goto(0, -304)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
