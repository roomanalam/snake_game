from turtle import Turtle
STARTING_POSITION =[(0,0),(-20,0),(-40,0)]
Move_pace =20
UP = 90
DOWN = 270
LEFT= 180
RIGHT = 0
class snake:

   def __init__(self):
     self.snake_segments =[]
     self.create_snake()
     self.head = self.snake_segments[0]

   def create_snake(self):  
     for pos in STARTING_POSITION:
        self.add_segment(pos)
      
    
   def add_segment(self,position):
       snake = Turtle(shape="square")
       snake.color("white")
       snake.penup()
       snake.goto(position)
       self.snake_segments.append(snake)

   def extend(self):
      self.add_segment(self.snake_segments[-1].position())

    
   def move(self):
     for seg in range(len(self.snake_segments)-1,0,-1):
       new_x= self.snake_segments[seg-1].xcor()  
       new_y = self.snake_segments[seg-1].ycor()
       self.snake_segments[seg].goto(new_x,new_y)  
      
     self.head.fd(Move_pace)  

   def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

   def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

   def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

   def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

   
   
