from cardClass import *
from random import *
from itertools import combinations

class player():
    def __init__(self,name):
        self.playerName=name
        self.hand=[]
    
    def name(self): return self.playerName

    def giveHand(self,hand): self.hand.extend(hand)
    
    def getHand(self): return self.hand

    def clearHand(self): self.hand=[]

    def __str__(self): return self.playerName

def main():
    game=True
    name=input("Enter your name:\n")
    if game:
        cardDeck=deck()
        player1=player(name)
        player2=player("Player 2")
        player3=player("Player 3")
        player4=player("Player 4")
        players=[player1,player2,player3,player4]
        pOrder=[]
        for i in range(4):
            pOrder.append(players.pop(randint(0,len(players)-1)))
        print("Player Order:\n", pOrder[0],"\n",pOrder[1],"\n",pOrder[2],"\n",pOrder[3])
        player1.giveHand(cardDeck.draw(2))
        print("Your hand contains a",player1.getHand()[0],"and a",player1.getHand()[1])
        player2.giveHand(cardDeck.draw(2))
        player3.giveHand(cardDeck.draw(2))
        player4.giveHand(cardDeck.draw(2))
        # betting
        cardDeck.draw(1)
        print("A card is burned.")
        community=cardDeck.draw(3)
        print(community)
        for i in range(2):
            # betting
            cardDeck.draw(1)
            print("A card is burned.")
            community.extend(cardDeck.draw(1))
            print(community)
        

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

"""
[[1,2,3],
[1,2,4],
[1,2,5],
[1,3,4],
[1,3,5],
[1,4,5],
[2,3,4],
[2,3,5],
[2,4,5],
[3,4,5]]
"""