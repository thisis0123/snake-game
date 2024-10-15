from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.shapesize(0.5,0.5)
        self.appear()

    def appear(self):
        random_x=random.randint(-360,360)
        random_y=random.randint(-260,260)
        self.goto(random_x,random_y)

        pass

    
