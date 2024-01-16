from turtle import Turtle, Screen
from random import *

sc = Screen()
sc.setup(500, 400)
bet = sc.textinput("Make Your Bet", "Which Turtle will win the race? Enter a color: ")
colors = ['red', 'cyan', 'blue', 'green', 'yellow']
rang = [-100, -50, 0, 50, 100]
race = False
turt = []


for i in range(0,5):
    red = Turtle(shape='turtle')
    red.color(colors[i])
    red.penup()
    red.goto(-230, rang[i])
    turt.append(red)

if bet:
    race = True

while race:

    for i in turt:
        if i.xcor() > 230:
            race = False
            win = i.pencolor()
            if win == bet:
                print(f"You've Won! The {win} turtle is the winner.")
            else:
                print(f"You've Lost! The {win} turtle is the winner.")

        i.forward(randint(0,10))



# green = Turtle()
# green.color('green')
# green.shape('turtle')
# green.penup()
# green.goto(-230, -50)
#
# yellow = Turtle()
# yellow.color("yellow")
# yellow.shape('turtle')
# yellow.penup()
# yellow.goto(-230, 0)
#
# blue = Turtle()
# blue.color('blue')
# blue.shape('turtle')
# blue.penup()
# blue.goto(-230, 50)
#
# cyan = Turtle()
# cyan.color('cyan')
# cyan.shape('turtle')
# cyan.penup()
# cyan.goto(-230,100)


# tim.color('cyan')
# def forward():
#     tim.forward(10)
#
# def backward():
#     tim.back(10)
#
# def clockwise():
#     tim.right(5)
#
# def anticlock():
#     tim.left(5)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#
# tim.pensize(3)
# sc.onkey(key='w', fun=forward)
# sc.onkey(key="s", fun=backward)
# sc.onkey(key="d", fun=clockwise)
# sc.onkey(key="a", fun=anticlock)
# sc.onkey(key="c", fun=clear)
# sc.listen()
sc.exitonclick()