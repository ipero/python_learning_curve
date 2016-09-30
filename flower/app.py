import turtle

def draw_square(length):
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(5)

    count = 0
    while(count<4):
        brad.forward(length)
        brad.right(90)
        count = count + 1

def draw_circle(rad):
    tony = turtle.Turtle()
    tony.shape("arrow")
    tony.color("blue")
    tony.speed(5)
    tony.circle(rad)


def draw_triangle(length):
    angie = turtle.Turtle()
    angie.color("#285078")

    angie.speed(5)
    angie.right(90)
    count = 0
    while(count<3):
        angie.bk(length)
        angie.right(120)
        count = count + 1

def draw_flower():
    pen = turtle.Turtle()
    pen.color("purple")
    #pen.setx(300)
    pen.sety(-250)
    pen.left(60)
    pen.forward(100)
    pen.right(40)
    pen.forward(100)
    pen.right(140)
    pen.forward(100)
    pen.right(40)
    pen.forward(100)

    pen.left(320)
    pen.forward(100)
    pen.right(40)
    pen.forward(100)
    pen.right(140)
    pen.forward(100)
    pen.right(40)
    pen.forward(100)


    pen.left(150)
    pen.fd(350)

    for n in range(0,72):

        pen.left(60)
        pen.forward(100)
        pen.right(40)
        pen.forward(100)
        pen.right(140)
        pen.forward(100)
        pen.right(40)
        pen.forward(100)
        n = n + 1
        pen.right(15)

draw_flower()

#draw_square(150)
#draw_circle(100)
#draw_triangle(100)
