from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, "bold")
TEXT_PATH = "highest_score.txt"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.highest = 0
        self.retrieve_highest()
        self.update_score()

    def score_up(self):
        self.score += 1
        if self.score > self.highest:
            self.highest = self.score
            self.update_highest()
        self.update_score()

    def retrieve_highest(self):
        with open(TEXT_PATH, mode="a+") as file:
            file.seek(0)
            content = file.read()
            if content != "":
                self.highest = int(content)
                print(content)
            file.close()
        
    def update_highest(self):
        with open(TEXT_PATH, mode="w") as file:
            file.write(f"{self.highest}")
            file.close()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}\t Highest: {self.highest}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER! :()", True, align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", True, align=ALIGNMENT, font=FONT)
        self.goto(0, -60)
        self.write(f"Highest Score: {self.highest}", True, align=ALIGNMENT, font=FONT)
