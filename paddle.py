from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_yp = self.ycor() + 40
        self.goto(self.xcor(), new_yp)


    def go_down(self):
        new_yn = self.ycor() - 40
        self.goto(self.xcor(), new_yn)

