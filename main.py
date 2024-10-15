from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreBoard



window=Screen()
window.setup(800,600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake1=Snake()
food=Food()
score=ScoreBoard()
game_on=True
while game_on:
    snake1.move()
    window.listen()
    window.onkey(snake1.move_up,"Up")
    window.onkey(snake1.move_down,"Down")
    window.onkey(snake1.move_right,"Right")
    window.onkey(snake1.move_left,"Left")
    if snake1.head.distance(food)<15:
        food.appear()
        snake1.make_it_longer()
        score.increase_score()
    
    time.sleep(0.1)
    window.update()

    if (snake1.head.xcor()>370 ) or (snake1.head.ycor()>270) or (snake1.head.xcor()<-370) or (snake1.head.ycor()<-270):
        score.game_over()
        game_on=False

    for i in snake1.turtles[0:len(snake1.turtles)-1:]:
        if snake1.head.distance(i)<10:
            score.game_over()
            game_on=False

        
    

window.exitonclick()