from tbgcentral import *
def room3():
    doorunlocked=False
    roomdone=False
    invlist="You don't have an item."

    while roomdone==False:

        print("You can:",*options, sep = ", ")
        action=input("What do you do? ")
        print("")

        if action=="1":
            print("This room 5 buttons, with a lantern corresponding to each button.\nThere is yet another locked door going forward, but this door has no keyhole on it.")
        
        elif action=="2":
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
            print("You don't have that.")


        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
            if interact=="button" or "buttons" and doorunlocked==False:
                lanternlist=[0,0,0,0,0]
                displaylist=["\u25CB","\u25CB","\u25CB","\u25CB","\u25CB"]
                x=1
                print(*displaylist)
                while x==1:
                    query=input("Which button will you press? (1, 2, 3, 4, 5, or exit): ")
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
                print("You can't interact with",interact)
        
        elif action=="5":
            move=input("Forward or back?")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.")
                    roomdone=True
                    return 4
                else:
                    print("The door is locked.")
            elif move=="back":
                print("The door closed behind you, and it will no longer open because you broke the lock.\nThere's no way to go back.")
            else:
                print("That wasn't an option.")
        else:
            print("Sorry, that wasn't an option.")

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