import sys
from pygame.locals import *
import time
# initialize pygame
# Example file showing a basic pygame "game loop"
import pygame
from cardClass import *
from pokerGame import *
# pygame setup
def main():
    pygame.init()
    money=1000
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    while running:
        pool=0
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        deck1=deck()
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("dark green")
        handGraphic=[pygame.image.load(deck1.draw(1)[0].cardGraphic()),pygame.image.load(deck1.draw(1)[0].cardGraphic())]
        for i,e in enumerate(handGraphic):
            screen.blit(e,(600+((i-1)*65),600))
        pygame.display.flip()
        amount=input("choose") # Work with buttons
        money-=amount
        pool+=4*amount
        running=pause(running)
        # RENDER YOUR GAME HERE
        deck1.draw(1)[0]
        flop=[pygame.image.load(deck1.draw(1)[0].cardGraphic()),pygame.image.load(deck1.draw(1)[0].cardGraphic()),pygame.image.load(deck1.draw(1)[0].cardGraphic())]
        for i,e in enumerate(flop):
            screen.blit(e,(600+((i-1)*65),300))
        # flip() the display to put your work on screen
        pygame.display.flip()
        amount=input("choose") # Work with buttons
        money-=amount
        pool+=4*amount
        
        deck1.draw(1)[0]
        turn=pygame.image.load(deck1.draw(1)[0].cardGraphic())
        screen.blit(turn,(730,300))
        pygame.display.flip()
        amount=input("choose") # Work with buttons
        money-=amount
        pool+=4*amount
        running=pause(running)
        river=pygame.image.load(deck1.draw(1)[0].cardGraphic())
        screen.blit(river,(795,300))
        pygame.display.flip()
        amount=input("choose") # Work with buttons
        money-=amount
        pool+=4*amount
        running=pause(running)
        clock.tick(60)  # limits FPS to 60
        

    pygame.quit()

def pause(running):
    wait=True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait=False
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                wait=False
                return running

main()

class button():
    def __init__(self,size,loc,color,text):
        self.buttonRect=pygame.Rect(loc[0],loc[1],size[0],size[1])
        self.color=color
        self.text=pygame.font.Font(None,28)
        self.textSurface=self.text.render(text,True,(0,0,0),None)
    def getRect(self): return self.buttonRect
    def getColor(self):return self.color
    def getTextSurface(self): return self.textSurface

class player():
    def __init__(self,name):
        self.playerName=name
        self.hand=[]
    
    def name(self): return self.playerName

    def giveHand(self,hand): self.hand.extend(hand)
    
    def getHand(self): return self.hand

    def __str__(self): return self.playerName