import turtle
turtle.speed(9)

t_init = turtle.Turtle()
turtle.bgcolor("white")
turtle.speed(9)

for i in range(50):

    for colors in ["red","yellow","green","blue","violet","orange","pink","purple"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        

