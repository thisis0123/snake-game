from turtle import Turtle


class Snake:
    def __init__(self):
        self.turtles=[]
        self.positions=[-40,-20,0]
        self.create()
        self.head=self.turtles[-1]
        
    def create(self):
        for i in range(len(self.positions)):
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.up()
            new_turtle.goto(self.positions[i],0)
            self.turtles.append(new_turtle)

    def make_it_longer(self):
        new_turtle=Turtle("square")
        new_turtle.color("white")
        new_turtle.up()
        new_turtle.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_turtle)
        self.positions.insert(0,self.positions[0]-20)



    def move(self):
        for i in range(len(self.positions)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)
        
    def move_up(self):
        self.head.setheading(90)

    def move_down(self):
        self.head.setheading(270)

    def move_right(self):
        self.head.setheading(0)

    def move_left(self):
        self.head.setheading(180)
