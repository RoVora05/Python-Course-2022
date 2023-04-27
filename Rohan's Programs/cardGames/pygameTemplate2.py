import sys
from pygame.locals import *
import time
# initialize pygame
# Example file showing a basic pygame "game loop"
import pygame
from cardClass import *
from pokerGame import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
money= 1000
cardDeck=deck()
flop=[]
stakes=0
playerList=[player("You"),player("Player 2"),player("Player 3"),player("Player 4")]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

def dealHands():
    for i in range(4):
        playerList[i].giveHand(cardDeck.draw(2))
    

def bet():1

def burn():
    cardDeck.draw()

def revealFlop():
    flop.extend(cardDeck.draw(3))

def turnRiver():
    flop.extend(cardDeck.draw(1))

def cleanUp():
    cardDeck.resetDeck()
    global flop
    flop=[]
    for i in range(4):
        playerList[i].clearHand()
    global stakes
    stakes=0
    if money<=0:
        gameOver()

def gameOver():
    1

class button():
    def __init__(self,size,loc,color,text):
        self.buttonRect=pygame.Rect(loc[0],loc[1],size[0],size[1])
        self.color=color
        self.text=pygame.font.Font(None,28)
        self.textSurface=self.text.render(text,True,(0,0,0),None)
    def getRect(self): return self.buttonRect
    def getColor(self):return self.color
    def getTextSurface(self): return self.textSurface