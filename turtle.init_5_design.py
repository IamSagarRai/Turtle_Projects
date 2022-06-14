import turtle

t = turtle.Turtle()
s = turtle.screen()

s.bgcolor("black")
s.pencolor("light green")

t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
t.pensize(2)

a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()

turtle.done()
