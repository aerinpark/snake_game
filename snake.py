from turtle import Turtle

RIGHT = 0
DOWN = 270
LEFT = 180
UP = 90

# left, right, down, up
LEFT_WALL = -281
RIGHT_WALL = 281
TOP_WALL = 281
BOTTOM_WALL = -281

class Snake:
    def __init__(self):
        self.body_parts = []
        x = -20
        self.head = Turtle("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(x, 0)
        self.body_parts.append(self.head)
        self.body_size = 3
        self.grow()
        self.grow()

    
    def move(self):
        for i in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[i - 1].xcor()
            new_y = self.body_parts[i - 1].ycor()
            self.body_parts[i].goto(new_x, new_y)
        self.head.forward(20)
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def wall_collision(self):
        if self.head.xcor() > RIGHT_WALL or self.head.xcor() < LEFT_WALL or self.head.ycor() > TOP_WALL or self.head.ycor() < BOTTOM_WALL:
            return True
        return False

    def grow(self):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(self.body_parts[-1].position())
        self.body_parts.append(new_body)
        self.body_size += 1

    def self_collision(self):
        for body in self.body_parts:
            if body == self.head:
                pass
            if self.head.distance(body) < 10:
                return True
        return False
        
        



