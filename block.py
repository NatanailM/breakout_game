from turtle import Turtle


class Block(Turtle):
    def __init__(self, x_cor, y_cor, color):
        super().__init__()

        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(2, 4.37)
        self.speed(0)
        self.goto(x_cor, y_cor)

    def destroy(self):
        self.goto(2000, 2000)
        self.clear()