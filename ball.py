from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.goto(0, -278)

        self.lives = 3
        self.launched = False
        self.speed_x = 10
        self.speed_y = 10

    def launch(self):
        if not self.launched:
            self.launched = True

    def move(self):
        if self.launched:
            new_x = self.xcor() - self.speed_x
            new_y = self.ycor() + self.speed_y
            self.goto(new_x, new_y)

    def bounce_x(self):
        self.speed_x *= -1

    def bounce_y(self):
        self.speed_y *= -1

    def lose_life(self):
        self.lives -= 1
        self.launched = False
        self.goto(0, -278)
