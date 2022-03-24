import turtle
a_init = turtle.Turtle()
s_n = turtle.Screen()
s_n.bgcolor('black')
col= ('white','orange','red','green','yellow','blue','cyan')
a_init.speed(0)

for i in range(200):
    a_init.forward(i*4)
    a_init.right(91)
    a_init.color(col[i%7])
    for b in range (3):
        a_init.forward(i*4)
        a_init.right(91)
        for c in range(2):
            a_init.forward(i*4)
            a_init.right(91)

