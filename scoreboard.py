from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",15, "normal")

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score =0
        self.goto(x=0,y=280) 
        self.score_refresh()

    def score_refresh(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,font= FONT)

    def gameover(self):
         self.goto(x=0,y=0) 
         self.write("GAME OVER", align=ALIGNMENT,font= FONT)

    def score_increment (self):
        self.score+= 1
        self.clear()
        self.score_refresh()
    

    