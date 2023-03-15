from turtle import Screen, Turtle
import time 

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.setposition(position)

    def go_up(self):
        y_axis = self.ycor()+20
        self.goto(self.xcor(),y_axis)

    def go_down(self):
        y_axis = self.ycor()-20
        self.goto(self.xcor(),y_axis)


class Ball(Turtle):
    def __init__(self): 
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
       new_x = self.xcor() + self.x_move 
       new_y = self.ycor() + self.y_move
       self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1 
    
    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0,0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier",80, "normal")) 
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier",80, "normal"))
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard() 

    def scorelimit(self):
        if self.r_score>4 or self.l_score>4:
            return False
        else:
            True
    
    def winner(self):
        if self.r_score > 4:
            self.goto(0,-100)
            self.write("GAME OVER!! right player won", align="center", font=("Courier", 30, "normal"))
        if self.l_score > 4:
            self.goto(0,-100)
            self.write("GAME OVER!! left player won", align="center", font=("Courier", 30, "normal"))
    

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((375,0))
l_paddle = Paddle((-375,0))
ball = Ball()
scoreboard = Scoreboard()

def r_move_up():
    y_axis = r_paddle.ycor() + 30
    r_paddle.goto(r_paddle.xcor(),y_axis)

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w") 
screen.onkey(l_paddle.go_down, "s")

sleep_time = 0.1
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()
    
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle)<50 and ball.xcor() < -340):
        ball.bounce_x()
        sleep_time = sleep_time*0.98

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    to_check = scoreboard.scorelimit()
    scoreboard.winner()

    if to_check == False:
        is_game_on = False
        
    
screen.exitonclick()