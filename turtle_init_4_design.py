import turtle

turtle.Screen().bgcolor("black")

t_init = turtle.Turtle()
t_init.speed(10)
t_init.pensize(10)
t_init.penup()

def d_a():
    t_init.setposition(0,-280)
    t_init.pendown()
    t_init.begin_fill()
    t_init.color('pink')
    t_init.pencolor('cyan')
    t_init.circle(300)
    t_init.end_fill()
    t_init.penup()

def d_b():
    t_init.pensize(2)
    t_init.setposition(0,-230)
    t_init.pendown()
    t_init.begin_fill()
    t_init.color('black')
    t_init.circle(250)
    t_init.end_fill()
    t_init.penup()




def d_c():
    t_init.setposition(30,-110)
    t_init.pendown()
    t_init.begin_fill()
    t_init.color('cyan')
    t_init.pensize(10)
    t_init.pencolor('white')
    t_init.forward(23)
    t_init.backward(123)
    t_init.left(60)
    t_init.backward(220)
    t_init.right(60)
    t_init.backward(100)
    t_init.right(117)
    t_init.backward(710)
    t_init.right(63)
    t_init.backward(110)
    t_init.right(90)
    t_init.backward(510)
    t_init.right(90)
    t_init.backward(100)
    t_init.right(90)
    t_init.backward(70)
    t_init.end_fill()
    t_init.penup()

def d_d():
    t_init.pensize(10)
    t_init.setposition(53,-40)
    t_init.pendown()
    t_init.begin_fill()
    t_init.color('black')
    t_init.pencolor('white')
    t_init.right(90)
    t_init.forward(100)
    t_init.right(115)
    t_init.forward(250)
    t_init.right(157)
    t_init.forward(227)
    t_init.end_fill()

def d_e():
    t_init.backward(80)
    t_init.left(42)
    t_init.forward(147)
    t_init.right(83)
    t_init.forward(140)

d_a()
d_b()
d_c()
d_d()
d_e()

t_init.hideturtle()
turtle.done()
