import time
import turtle as t

from block import Block
from paddle import Paddle
from ball import Ball


def update_lives():
    score.clear()
    score.color("white")
    score.goto(-330, 270)
    score.write(f"LIVES: {ball.lives}", True, font=("Courier", 32, "normal"))
    score.goto(-330, 270)
    score.write(f"LIVES: {ball.lives}", True, font=("Courier", 32, "normal"))


def game_over():
    global game_on
    over = t.Turtle()
    over.penup()
    over.color("white")
    over.goto(-120, -100)
    over.write("GAME OVER", True, font=("Courier", 32, "normal"))
    game_on = False


def win():
    global game_on
    over = t.Turtle()
    over.penup()
    over.color("white")
    over.goto(-120, -100)
    over.write("YOU WIN", True, font=("Courier", 32, "normal"))
    game_on = False


colors = ["purple", "blue", "green", "yellow", "orange", "red"]

window = t.Screen()
window.title("Breakout")
window.bgcolor("black")
window.tracer(0)


paddle = Paddle()
ball = Ball()

score = t.Turtle()
score.color("white")
score.speed(0)
score.hideturtle()
score.penup()
score.goto(-350, 270)
update_lives()

blocks = []

x_cor = -330
y_cor = 0
for k in range(6):
    for i in range(8):
        new_block = Block(x_cor, y_cor, colors[k])
        x_cor += 93
        blocks.append(new_block)
    x_cor = -330
    y_cor += 45


window.listen()

window.onkeypress(paddle.move_left, "Left")
window.onkeypress(paddle.move_right, "Right")
window.onkeypress(ball.launch, "space")

game_on = True

while game_on:
    window.update()
    time.sleep(0.020)
    ball.move()

    if paddle.xcor() < -280:
        paddle.setx(-280)

    if paddle.xcor() > 280:
        paddle.setx(280)

    if ball.xcor() < -365 or ball.xcor() > 365:
        ball.bounce_x()

    if ball.ycor() < -310 or ball.ycor() > 310:
        ball.bounce_y()

    if ball.ycor() < -278 and ball.distance(paddle) < 130:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.lose_life()
        paddle.goto(0, -304)
        update_lives()

    for block in blocks:
        if ball.distance(block) < 45:
            block.destroy()
            blocks.remove(block)
            ball.bounce_y()
            if len(blocks) == 0:
                win()

    if ball.lives == 0:
        game_over()


t.mainloop()
