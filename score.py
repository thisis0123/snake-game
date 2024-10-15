from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.up()
        self.color("white")
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align="center",font=("arial",24,"normal"))

    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.screen.bgcolor("red")
        self.goto(0,0)
        self.write(f"Game Over\nFinal Score: {self.score}",align="center",font=("arial",24,"normal"))


