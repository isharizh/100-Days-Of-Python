from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
heads = 20
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    def __init__(self):
        self.seg =[]
        self.create()
        self.head = self.seg[0]

    def create(self ):
        for i in pos:
            self.add_segment(i)

    def add_segment(self,pos):
        tim = Turtle()
        tim.color('white')
        tim.penup()
        tim.shape('square')
        tim.goto(pos)
        self.seg.append(tim)

    def move(self):

        for i in range(len(self.seg) - 1, 0, -1):
            x = self.seg[i - 1].xcor()
            y = self.seg[i - 1].ycor()
            self.seg[i].goto(x, y)
        self.head.forward(heads)

    def extend(self):
        self.add_segment(self.seg[-1].pos())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)