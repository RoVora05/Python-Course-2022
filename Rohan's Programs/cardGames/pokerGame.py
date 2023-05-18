from cardClass import *
from random import *

class player():
    def __init__(self,name):
        self.playerName=name
        self.hand=[]
        self.chosenCards=[]
    
    def name(self): return self.playerName
    def giveHand(self,hand): self.hand.extend(hand)
    def getHand(self): return self.hand
    def clearHand(self): self.hand=[]
    def giveChosenCards(self,chosenCards): self.chosenCards.extend(chosenCards)
    def getChosenCards(self): return self.chosenCards
    def fullHandConvert(self): self.chosenCards.extend(self.hand)
    def giveHandValue(self,handValue):self.handValue=handValue
    def getHandValue(self): return self.handValue
    def giveHandName(self,name): self.handName=name
    def getHandName(self): return self.handName

    def __str__(self): return self.playerName

def main():
    game=True
    bigWins=0
    wins=0
    loses=0
    money=100
    stakes=0
    while game:
        cardDeck=deck()
        playerList=[player("You"),player("Player 2"),player("Player 3"),player("Player 4")]
        playerList[0].giveHand(cardDeck.draw(2))
        input("Your hand contains the "+str(playerList[0].getHand()[0])+" and the "+str(playerList[0].getHand()[1])+".")
        print()
        playerList[1].giveHand(cardDeck.draw(2))
        playerList[2].giveHand(cardDeck.draw(2))
        playerList[3].giveHand(cardDeck.draw(2))
        betVal=bet(money)
        stakes+=4*betVal
        money-=betVal
        cardDeck.draw(1)
        input("A card is burned.")
        print()
        community=cardDeck.draw(3)
        print("The flop is:")
        print("1. "+str(community[0]))
        print("2. "+str(community[1]))
        print("3. "+str(community[2]))
        input("\nYour hand contains the "+str(playerList[0].getHand()[0])+" and the "+str(playerList[0].getHand()[1])+".")
        print()
        for i in range(2):
            betVal=bet(money)
            stakes+=4*betVal
            money-=betVal
            cardDeck.draw(1)
            input("A card is burned.")
            print()
            community.extend(cardDeck.draw(1))
            if len(community)==4:
                print("The flop is:")
                print("1. "+str(community[0]))
                print("2. "+str(community[1]))
                print("3. "+str(community[2]))
                print("4. "+str(community[3]))
                input("\nYour hand contains the "+str(playerList[0].getHand()[0])+" and the "+str(playerList[0].getHand()[1])+".")
                print()
            else:
                print("The flop is:")
                print("1. "+str(community[0]))
                print("2. "+str(community[1]))
                print("3. "+str(community[2]))
                print("4. "+str(community[3]))
                print("5. "+str(community[4]))
                input("\nYour hand contains the "+str(playerList[0].getHand()[0])+" and the "+str(playerList[0].getHand()[1])+".")
                print()
        
        cardsUsed=[]
        for i in range(3):
            sentinel=True
            while sentinel:
                cardToAdd=input("Pick a card to use in your final hand:\n")
                if cardToAdd=='':
                    input("You must enter a value.")
                else:
                    cardToAdd=int(cardToAdd)
                    if cardToAdd<1 or cardToAdd>5:
                        input("Number must be between 1 and 5.")
                    elif cardToAdd in cardsUsed:
                        input("You already used this card!")
                    else:
                        cardsUsed.append(cardToAdd)
                        sentinel=False
                    print()
        
        playerList[0].giveChosenCards([community[cardsUsed[0]-1],community[cardsUsed[1]-1],community[cardsUsed[2]-1]])
        playerList[0].fullHandConvert()
        value,name=checkHand(playerList[0].getChosenCards())
        playerList[0].giveHandValue(value)
        playerList[0].giveHandName(name)
        
        for i in range(1,4):
            chosen,value,name=chooseCardsList(community,playerList[i].getHand())
            playerList[i].giveChosenCards(chosen)
            playerList[i].giveHandValue(value)
            playerList[i].giveHandName(name)
    
        sortedPlayerList=sorted(playerList, key=lambda e:e.getHandValue())
        sortedPlayerList.reverse()
        print(str(sortedPlayerList[0])+" won with a "+str(sortedPlayerList[0].getHandName())+"!\n")
        placement=["1st Place: ","2nd Place: ","3rd Place: ","4th Place: "]
        for i,e in enumerate(sortedPlayerList):
            print(placement[i]+str(e)+" - "+str(e.getChosenCards()[0]),str(e.getChosenCards()[1]),str(e.getChosenCards()[2]),str(e.getChosenCards()[3]),str(e.getChosenCards()[4]), sep=", ")
        print()

        if sortedPlayerList[0].name()=="You":
            money+=stakes
            wins+=1
            print("You won $"+str(stakes))
        else: loses+=1
        stakes=0
        input("You now have $"+str(money))
        print()
        if money<=0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("GAME OVER\nYou ran out of money!")
            game=False
        elif money>=1000 and bigWins==0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            input("You turned $100 into $1000!\nYou won",wins,"games and lost",loses,"games.")
            bigWins+=1
            game=False

def bet(money):
    while True:
        print("\nYou have $"+str(money))
        if money<=0:
            input("You bet $1 because you are broke.")
            return 1
        else:
            bet=input("Enter the value of your bet:\n")
            if bet=='':
                input("You must enter a value.")
            else:
                bet=int(bet)
                if bet<=0: 
                    input("You must bet a positive amount.")
                else:
                    input("The other players match your bet.")
                    print()
                    return bet

def chooseCardsList(community,hand):
    combination=[[community[0],community[1],community[2]],[community[0],community[1],community[3]],[community[0],community[1],community[4]],[community[0],community[2],community[3]],[community[0],community[2],community[4]],[community[0],community[3],community[4]],[community[1],community[2],community[3]],[community[1],community[2],community[4]],[community[1],community[3],community[4]],[community[2],community[3],community[4]]]
    for i in range(len(combination)): combination[i].extend(hand)
    value=0
    bestHand=0
    for e in combination:
        c,name=checkHand(e)
        if c>value:
            bestHand=e
            value=c
            handName=name
    return bestHand, value, handName

main()