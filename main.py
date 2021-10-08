from turtle import Turtle ,Screen
from snake import snake
from food import Food
from scoreboard import score
import time

screen = Screen ()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = snake()
food = Food()
score = score()



screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")



screen.update()
is_game_on =True

while is_game_on:
     screen.update()
     time.sleep(0.1)
     snake.move()

     #Detect the food collision
     if snake.head.distance(food)<15:
          food.refresh()
          snake.extend()
          score.score_increment()

     #Detect the wall collision
     if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
          is_game_on = False
          score.gameover()

     #Detect the collision with tail   
     for segment in snake.snake_segments[1:]:
          if snake.head.distance(segment)<10:
                is_game_on = False
                score.gameover()

     
     




















screen.exitonclick()