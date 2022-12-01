from tbgcentral import *
def room1():
    hasKey=False
    doorunlocked=False
    roomdone=False
    invlist="You don't have an item."
    while roomdone==False:

        print("You can:",*options, sep = ", ")
        action=input("What do you do? ")
        print("")

        if action=="1":
            print("There's nothing interesting in this room, just some sort of receptionist desk with a key on it and a locked door going forward.\nI really hope you can put this together, or this might take a while.")
        
        elif action=="2":
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
            if useitem=="key" and hasKey==True:
                print("The key fits into the door's lock, and immediately breaks.\nPoor quality key, but at least the door is open.")
                doorunlocked=True
                hasKey=False
                invlist="You don't have an item."
            else:
                print("You don't have that.")


        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
            if interact=="key" or "desk":
                print("You pick up the key.")
                hasKey=True
                invlist="It's a key. You found on the desk."
            else:
                print("You can't interact with",interact)
        
        elif action=="5":
            move=input("Forward or back?")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.")
                    roomdone=True
                    return 2
                else:
                    print("The door is locked.")
            elif move=="back":
                print("There's only one door in this room, and it goes forward.")
            else:
                print("That wasn't an option.")
        else:
            print("That wasn't an option.")

        print("")