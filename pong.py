import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong Game by progenor aka Wojtek")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#PADDLE_A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#PADDLE_B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.13
ball.dy = 0.13

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player_A: 0  Player_B :0", align="center", font=("Curier", 22, "normal"))



#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    yb = paddle_b.ycor()
    yb +=20
    paddle_b.sety(yb)

def paddle_b_down():
    yb = paddle_b.ycor()
    yb -= 20
    paddle_b.sety(yb)

#Keyboard biding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main cucc
while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player_A: {}  Player_B : {}".format(score_a, score_b), align="center", font=("Curier", 22, "normal"))
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player_A: {}  Player_B : {}".format(score_a, score_b), align="center", font=("Curier", 22, "normal"))
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

##### paddle and ball col
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #score sheck
    if score_a == 5:
        win = turtle.Turtle()
        win.speed(0)
        win.color("white")
        win.penup()
        win.hideturtle()
        ball.hideturtle()
        paddle_b.hideturtle()
        paddle_a.hideturtle()
        win.write("Player A won the game!!", align="center", font=("Curier", 32, "normal"))
        winsound.PlaySound("win_song.wav", winsound.SND_ALIAS)
    elif score_b == 5:
        win = turtle.Turtle()
        win.speed(0)
        win.color("white")
        win.penup()
        win.hideturtle()
        ball.hideturtle()
        paddle_b.hideturtle()
        paddle_a.hideturtle()
        win.write("Player B won the game!!", align="center", font=("Curier", 32, "normal"))
        winsound.PlaySound("win_song.wav", winsound.SND_ALIAS)


