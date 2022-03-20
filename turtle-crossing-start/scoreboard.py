from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-240,270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)