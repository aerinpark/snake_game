from turtle import Turtle
import random

class Food(Turtle):    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("pink")
        self.speed("slowest")
        self.set_location()
    
    def set_location(self):
        self.goto(round(random.uniform(-7, 7)) * 40, round(random.uniform(-7, 6)) * 40)


