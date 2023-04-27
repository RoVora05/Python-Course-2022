from random import *
from collections import Counter
import os
class card():
    def __init__(self,rank,suite):      
        self.rank=str(rank)
        self.loc="Cards\\"+str(rank)+suite[0]+".png" # 64 x 89 pixels
        if rank==1:
            self.rank="Ace"
            rank=14
        elif rank==11:
            self.rank="Jack"
        elif rank==12:
            self.rank="Queen"
        elif rank==13:
            self.rank="King"
        self.rawRank=rank
        self.suite=suite
        
    def cardRank(self): return self.rank
    def cardRawRank(self): return self.rawRank
    def cardSuite(self): return self.suite
    def cardGraphic(self): return self.loc
    def __str__(self): return self.rank+" of "+self.suite

class deck():
    def __init__(self):
        self.orderedList=[]
        for i in range(13):
            for e in ["Clubs","Diamonds","Hearts","Spades"]:
                self.orderedList.append(card(i+1,e))
        self.shuffle()

    def resetDeck(self):
        for i in range(13):
            for e in ["Clubs","Diamonds","Hearts","Spades"]:
                self.orderedList.append(card(i+1,e))
        self.shuffle()

    def shuffle(self): 
        List=self.orderedList
        self.orderedList=[]
        for i in range(len(List)): 
            self.orderedList.append(List.pop(randint(0,len(List)-1)))

    def order(self):
        return self.orderedList

    def draw(self,n):
        drawnCards=[]
        for i in range(n):
            drawnCards.append(self.orderedList.pop(0))
        return drawnCards

def checkHand(hand):
    handSuites=[e.cardSuite() for e in hand]
    handRank=[e.cardRawRank() for e in hand]
    rankC=Counter(handRank)
    sortedHand=sorted(handRank)
    sortedHandName=sorted(hand, key=lambda e:e.cardRawRank())
    pairs=0
    three=False
    four=False
    flush=False
    straight=True
    for e in rankC:
        if rankC[e]==2:
            pairs+=1
        elif rankC[e]==3:
            three=True
        elif rankC[e]==4:
            four=True
    
    suiteC=Counter(handSuites)
    for e in suiteC:
        if suiteC[e]==5:
            flush=True
    
    for i,e in enumerate(sortedHand):
        if sortedHand[0]+i==e: 1
        else:
            straight=False
    if sortedHand==[2,3,4,5,14]:
        straight=True

    print()
    if straight and flush and sortedHand[0]==10:
        return 10
    elif straight and flush:
        return 9
    elif four:
        return 8
    elif three and pairs==1:
        return 7
    elif flush:
        return 6
    elif straight:
        return 5
    elif three:
        return 4
    elif pairs==2:
        return 3
    elif pairs==1:
        return 2
    else:
        return 0.1*sortedHand[-1]

cardBack="Cards/backR.png"