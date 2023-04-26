import turtle 
from turtle import *
import random
from game_controller import *

## Fenster benennen


# Player1
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)

# Player2
player_two = turtle.Turtle()
player_two.color("blue")
player_two.shape("turtle")
player_two.penup()
player_two.goto(-200,-100)


# Zeig mir dein Zuhause Player1
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

# Zeig mir dein Zuhause Player2
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)


init([player_one, player_two])
start_game()

#turtle.Screen().exitonclick()