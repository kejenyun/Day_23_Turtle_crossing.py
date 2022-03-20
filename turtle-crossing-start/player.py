STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.setpos(STARTING_POSITION)

    def is_at_fihish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False


