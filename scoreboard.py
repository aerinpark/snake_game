from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
    
    def score_up(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 20, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER! :()", True, align="center", font=('Arial', 20, "bold"))
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", True, align="center", font=('Arial', 20, "bold"))