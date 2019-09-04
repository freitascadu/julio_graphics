import turtle

tuga = turtle.Turtle()
tuga.color("red","yellow")
tuga.speed(0)

tuga.begin_fill()
for i in range(180):
    tuga.forward(200)
    tuga.left(190)
tuga.end_fill()

turtle.done()
