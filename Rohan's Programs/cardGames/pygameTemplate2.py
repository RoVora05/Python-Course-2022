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
state=0
gameOrder=["dealHands","bet","burn","revealFlop","bet","burn","turnRiver","bet","burn","turnRiver","payOut"]
playerList=[player("You"),player("Player 2"),player("Player 3"),player("Player 4")]
def main():
    global screen
    global state
    nextbutton=button(size,loc,"white",">",textSize)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("dark green")
        if gameOrder[state]=="dealHands":
            if playerList[0].getHand()==[]:dealHands()
            else:
                handGraphic=[pygame.image.load(playerList[0].getHand()[0]),pygame.image.load(playerList[0].getHand()[1])]
                for i,e in enumerate(handGraphic):
                    screen.blit(e,) # define coordinates
                nextbutton.drawButton(screen)
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if nextbutton.getRect().collidepoint(pygame.mouse.get_pos()):
                        state+=1
        elif gameOrder[state]=="bet":
            bet(screen)
        elif gameOrder[state]=="burn":
            burn()
        elif gameOrder[state]=="revealFlop":
            revealFlop()
        elif gameOrder[state]=="turnRiver":
            turnRiver()
        elif gameOrder[state]=="payOut":
            payOut()            
        elif state==11:
            if money<=0:
                gameOver()
            else:
                cleanUp()
        # RENDER YOUR GAME HERE
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

def dealHands():
    for i in range(4):
        playerList[i].giveHand(cardDeck.draw(2))

def bet(screen):
    global money
    global stakes
    size,loc,textSize=0 # define coordinates
    b0=button(size,loc,"white","None",textSize)
    b20=button(size,loc,"white","20",textSize)
    b50=button(size,loc,"white","50",textSize)
    b100=button(size,loc,"white","100",textSize)
    b250=button(size,loc,"white","250",textSize)
    bL=[b0,b20,b50,b100,b250]
    for e in bL:
        e.drawButton(screen)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousePos=pygame.mouse.get_pos()
            if b0.getRect().collidepoint(mousePos):
                money-=0
                stakes+=0
            if b20.getRect().collidepoint(mousePos):
                money-=20
                stakes+=80
            if b50.getRect().collidepoint(mousePos):
                money-=50
                stakes+=200
            if b100.getRect().collidepoint(mousePos):
                money-=100
                stakes+=400
            if b250.getRect().collidepoint(mousePos):
                money-=250
                stakes+=1000


def burn():
    cardDeck.draw()

def revealFlop():
    flop.extend(cardDeck.draw(3))

def turnRiver():
    flop.extend(cardDeck.draw(1))

def payOut():
    # player picks cards, is assigned hand value
    for i in range(3):
        value,chosenCards=chooseCardsList(flop,playerList[i+1].getHand())
        playerList[i+1].giveChosenCards(chosenCards)
        playerList[i+1].giveHandValue(value)
    sortedPlayerList=sorted(playerList, key=lambda e:e.getHandValue())
    if sortedPlayerList[-1].name()=="You":
        global money
        money+=stakes
    

def cleanUp():
    global flop
    global stakes
    global money
    cardDeck.resetDeck()
    flop=[]
    for i in range(4):
        playerList[i].clearHand()
    stakes=0
    if money<=0:
        gameOver()
    else: 
        global state
        state=0

def gameOver():
    text=pygame.font.Font(None,30)
    textSurface=text.render(text,True,(0,0,0),None)
    screen.blit(textSurface,(400,300))

def chooseCardsList(community,hand):
    combinations=list(combinations(community,3))
    for i in range(len(combinations)): combinations[i].extend(hand)
    value=0
    bestHand=0
    for e in combinations:
        c=checkHand(e)
        if c>value:
            bestHand=e
            value=c
    return value,bestHand

class button():
    def __init__(self,size,loc,color,text,textSize):
        self.buttonRect=pygame.Rect(loc[0],loc[1],size[0],size[1])
        self.color=color
        self.text=pygame.font.Font(None,textSize)
        self.textSurface=self.text.render(text,True,(0,0,0),None)
    def getRect(self): return self.buttonRect
    def getColor(self):return self.color
    def getTextSurface(self): return self.textSurface
    def drawButton(self,screen):
        screen.fill(self.color,self.buttonRect)
        screen.blit(self.textSurface,self.buttonRect)

class clickable():
    def __init__(self,card,loc):
        self.card=card
        self.surface=card.cardGraphic()
        self.loc=