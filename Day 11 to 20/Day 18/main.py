from turtle import Turtle, Screen, colormode
from random import *



tim = Turtle()
tim.shape('triangle')
tim.speed(100)
# tim.color("dark orchid")
rgb = []
for i in range(20):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tu = (r, g, b)
    rgb.append(tu)

def loop():

    colormode(255)
    for i in range(10):
        tim.color(choice(rgb))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.sety(50)


for i in range(0,500,50):
    tim.hideturtle()
    tim.penup()
    tim.setpos(-225,-200+i )
    loop()


# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
# color =["red", 'cyan',"dark orchid","coral", "black", "yellow", "green", "blue"]
# ran = [0, 90, 180, 270]
# tim.pensize(15)
# colormode(255)
# def colour():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     tu = (r, g, b)
#     return tu
#
# def san(size):
#     for i in range(int(360/size)):
#         tim.color(colour())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size)
# san(5)

# for i in range(1000):
#     tim.color(colour())
#     tim.forward(30)
#     tim.setheading(choice(ran))


    # tim.color(choice(color))
    # ran = randint(0,2)
    # if ran == 0:
    #     tim.forward(50)
    #
    # elif ran == 1:
    #     tim.right(90)
    # else:
    #     tim.left(90)

# count = 0
# for i in range(3,11):
#     an = round(360/i)
#     tim.color(color[count])
#     for j in range(0, i):
#         tim.forward(100)
#         tim.right(an)
#     count += 1
# for i in range(100):





sc = Screen()
sc.exitonclick()