from tbgcentral import *
def room2():
    hasNeedle=False
    doorunlocked=False
    roomdone=False
    invlist="You don't have an item."
    while roomdone==False:

        print("You can:",*options, sep = ", ")
        action=input("What do you do? ")
        print("")

        if action=="1":
            print("The only thing in this room is a stack of hay.\nThere is a locked door going forward again.")
        
        elif action=="2":
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
            if useitem=="needle" and hasNeedle==True:
                print("You try to pick the lock, only to realize that you don't know how to pick locks.\nBoth the needle and the lock break, and the door opens.")
                doorunlocked=True
                hasNeedle=False
                invlist="You don't have an item."

            else:
                print("You don't have that.")

        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
            if interact=="hay" or "haystack":
                print("You dig through the haystack and find a needle.\nIronic.")
                hasNeedle=True
                invlist="It's a needle. You don't want to think about how you got it."
            else:
                print("You can't interact with",interact)
        
        elif action=="5":
            move=input("Forward or back?")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.")
                    roomdone=True
                    return 3
                else:
                    print("The door is locked.")
            elif move=="back":
                print("The key you used to get in here broke, and the door closed behind you.\nIt seems like the only keyhole was on the other side of the door too, so there's no way to go back.")
            else:
                print("That wasn't an option.")
        else:
            print("Sorry, that wasn't an option.")

        print("")