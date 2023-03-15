from codecs import replace_errors
from turtle import Turtle, Screen
import random

screen = Screen()
user_guess = screen.textinput(title="make a bet", prompt = "which one will win the race?")
screen.setup(width = 500, height = 400)
colors = ["red", "blue", "green", "violet","black","brown"]
x = -230
y = -125
all_turtles =[]
for index in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.color(colors[index])
    y += 50
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print("you won the game!!")
            else:
                print(f"you lost the game!! the winning turtle is {winning_color}")
        rand_speed = random.randint(0,10)
        turtle.forward(rand_speed)

        
screen.exitonclick()
