def main():
    global options
    options=["1. look around","2. check item","3. use item","4. interact with environment","5. move"]

    print("You wake up in your room in the dungeon.\nAgain.\nIt's probably time to get out of here.\n")
    room1()
    room2()
    room3()
    print("You step out into the sunlight, after what feels like ages.\n...\nSeriously?\nYou were sitting in that dungeon for who knows how long, and all it took to escape was going through 3 unguarded rooms?\nYou started in a room where the key was literally right in front of you.\nThis makes you irrationally upset.\n...\n\nGAME OVER")

    
def room1():
    hasKey=False
    doorunlocked=False
    roomdone=False
    invlist="You don't have an item."
    keyGrabbed=False
    while roomdone==False:

        print("You can:",*options, sep = ", ")
        action=input("What do you do?\n")
        print("")

        if action=="1":
            print("There's nothing interesting in this room, just some sort of receptionist desk with a key on it and a locked door going forward.\nI really hope you can put this together, or this might take a while.")
        
        elif action=="2":
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use?\n")
            if useitem=="key" and hasKey==True:
                print("The key fits into the door's lock, and immediately breaks.\nPoor quality key, but at least the door is open.")
                doorunlocked=True
                hasKey=False
                invlist="You don't have an item."
            else:
                print("You don't have that.")


        elif action=="4":
            interact=input("What in the room would you like to interact with?\n")
            if interact=="key" and keyGrabbed==False:
                print("You pick up the key.")
                hasKey=True
                keyGrabbed=True
                invlist="It's a key. You found on the desk."
            else:
                print("You can't interact with that.")
        
        elif action=="5":
            move=input("Forward or back?\n")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.\n")
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
    
def room2():
    hasNeedle=False
    doorunlocked=False
    roomdone=False
    needleGrabbed=False
    invlist="You don't have an item."
    while roomdone==False:

        print("You can:",*options, sep = ", ")
        action=input("What do you do?\n")
        print("")

        if action=="1":
            print("The only thing in this room is a stack of hay.\nThere is a locked door going forward again.")
        
        elif action=="2":
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use?\n")
            if useitem=="needle" and hasNeedle==True:
                print("You try to pick the lock, only to realize that you don't know how to pick locks.\nBoth the needle and the lock break, and the door opens.")
                doorunlocked=True
                hasNeedle=False
                invlist="You don't have an item."

            else:
                print("You don't have that.")

        elif action=="4":
            interact=input("What in the room would you like to interact with?\n")
            if (interact=="hay" or interact=="haystack") and needleGrabbed==False:
                print("You dig through the haystack and find a needle.\nIronic.")
                hasNeedle=True
                needleGrabbed=True
                invlist="It's a needle. Don't think about how you got it."
            else:
                print("You can't interact with that.")
        
        elif action=="5":
            move=input("Forward or back?\n")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.\n")
                    roomdone=True
                    return 3
                else:
                    print("The door is locked.")
            elif move=="back":
                print("The key you used to get in here broke, and the door closed behind you.\nIt seems like the only keyhole was on the other side of the door too, so there's no way to go back.")
            else:
                print("That wasn't an option.")
        else:
            print("That wasn't an option.")

        print("")

def room3():
    doorunlocked=False
    roomdone=False
    invlist="You don't have an item."

    while roomdone==False:

        print("You can:",*options, sep = ", ")
        action=input("What do you do?\n")
        print("")

        if action=="1":
            print("This room 5 buttons, with a lantern corresponding to each button.\nThere is yet another locked door going forward, but this door has no keyhole on it.")
        
        elif action=="2":
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use?\n")
            print("You don't have that.")


        elif action=="4":
            interact=input("What in the room would you like to interact with?\n")
            if (interact=="button" or interact=="buttons") and doorunlocked==False:
                lanternlist=[0,0,0,0,0]
                displaylist=["\u25CB","\u25CB","\u25CB","\u25CB","\u25CB"]
                x=1
                print(*displaylist)
                while x==1:
                    query=input("Which button will you press? (1, 2, 3, 4, 5, or exit):\n")
                    if query=="exit":
                        x=0
                    else:
                        button=eval(query)
                        if 1<=button<=5:
                            button-=1
                            lanternListEditor(button,lanternlist)
                        else:
                            print("Invalid input.")
                    
                    for i,e in enumerate(lanternlist):
                        if e%2==0:
                            displaylist[i]="\u25CB"
                        else:
                            displaylist[i]="\u25CF"
                    print(*displaylist)
                    if displaylist==["\u25CF","\u25CF","\u25CF","\u25CF","\u25CF"]:
                        print("You hear the lock in the door click.")
                        x=0
                        doorunlocked=True
            else:
                print("You can't interact with that.")
        
        elif action=="5":
            move=input("Forward or back?\n")
            if move=="forward":
                if doorunlocked==True:
                    print("You move forward.\n")
                    roomdone=True
                    return 4
                else:
                    print("The door is locked.")
            elif move=="back":
                print("The door closed behind you, and it will no longer open because you broke the lock.\nThere's no way to go back.")
            else:
                print("That wasn't an option.")
        else:
            print("That wasn't an option.")

        print("")

def lanternListEditor(lantern,list):
    if lantern==0:
        list[4]+=1
        list[0]+=1
        list[1]+=1
    elif lantern==4:
        list[3]+=1
        list[4]+=1
        list[0]+=1
    else:
        list[lantern-1]+=1
        list[lantern]+=1
        list[lantern+1]+=1
    return list

main()