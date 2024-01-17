from turtle import Turtle, Screen
import time
from Snake import Snake
from food import Food
from score import Score


sc = Screen()
sc.setup(600, 600)
sc.bgcolor('black')
sc.title('Zyle Game')
sc.tracer(0)

sn = Snake()
f = Food()
s = Score()

sc.listen()
sc.onkey(sn.up, "Up")
sc.onkey(sn.down,"Down")
sc.onkey(sn.left, "Left")
sc.onkey(sn.right, "Right")


race = True

while race:
    sc.update()
    time.sleep(0.1)
    sn.move()
    if sn.head.distance(f) < 15:
        f.re()
        sn.extend()
        s.increase()

    if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        race = False
        s.col()

    for i in sn.seg[1:]:
        if sn.head.distance(i) < 10:
            race = False
            s.col()
sc.exitonclick()