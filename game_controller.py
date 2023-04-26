import turtle 
from turtle import *
import random
import time
from functools import partial

# global die
# global players
# global currentPlayer

def erasableWrite(x,y, msg, vanishSec, color, reuse=None):
    
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.clear() 
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(x,y)
    eraser.color(color)
    eraser.write(msg, font=("Cooper Black", 25, "italic"), align="center")
    
    if vanishSec > 0:
        time.sleep(vanishSec)
        eraser.clear()
         
    return eraser


currentPlayer=0
winner = False


def init(p):
    global die 
    die = [1,2,3,4,5,6]
    
    global players
    players=p
    
def writeMessage(msg):
    penup()
    setposition(0, 200)
    hideturtle()
    write(msg, align="center", font=("Cooper Black", 25, "italic"))


        
def enter(erasable):
    global currentPlayer
    global winner
    
    if winner==False:
        
        print("CurrentPlayer "+ str(currentPlayer))
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        
        erasableWrite(0,200,"Würfel: "+ str(die_outcome),1,players[currentPlayer].color()[0],erasable)
        players[currentPlayer].fd(20*die_outcome)
        
        if players[0].pos() >= (300,100):
                print("Player One Wins!")
                erasableWrite(0,200,"Player 1 WINS!",0,players[currentPlayer].color()[0],erasable)
                winner=True
        elif players[1].pos() >= (300,-100):
                print("Player Two Wins!")
                erasableWrite(0,200,"Player 2 WINS!",0,players[currentPlayer].color()[0],erasable)
                winner=True
        currentPlayer=(currentPlayer+1)%2
        
        if winner == False:
                erasableWrite(0,200,"Player "+ str(currentPlayer+1) +" bitte würfeln (ENTER drücken)",0,players[currentPlayer].color()[0],erasable)
     
def start_game():
    
    #writeMessage("Player 1 bitte würfeln (ENTER drücken)")
    eraseble = erasableWrite(0,200, "Hi! let's start he game!",2,"black")
         
    erasableWrite(0,200,"Player "+ str(currentPlayer+1) +" bitte würfeln (ENTER drücken)",0,players[currentPlayer].color()[0],eraseble)
    listen()
    #writeMessage("Player "+ str(currentPlayer+1) +"bitte würfeln (ENTER drücken)")
    onkey(partial(enter, eraseble), "z")
    mainloop()
            