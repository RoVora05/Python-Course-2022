from random import *

def playOneRound(prob):
    if (random()<prob):
        return 1
    else:
        return 0

def simVBallGame(aProb,bProb):
    winner=0
    aScore=0
    bScore=0
    while winner==0:
        while winner==0:
            if playOneRound(aProb)==1:
                aScore+=1
                print("Team A scores!")
                if aScore>14 and bScore+2<aScore:
                    winner="A!"
            else:
                break
        while winner==0:
            if playOneRound(bProb)==1:
                bScore+=1
                print("Team B scores!")
                if bScore>14 and aScore+2<bScore:
                    winner="B!"
            else:
                break
    print("The winner was team",winner)
    print("Team A scored",aScore,"points, and team B scored",bScore,"points.")

simVBallGame(0.8,0.8)