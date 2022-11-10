from tbgcentral import *
def room2():
    doorunlocked=False

    roomdone=False
    while roomdone==False:
        
        invread=open(file_location+"inventory.txt","r")
        invlist=invread.read().splitlines()

        invapp=open(file_location+"inventory.txt","a")
        
        invwrite=open(file_location+"inventory.txt","w")
        

        print("You can:",*options, sep = ", ")
        action=input("What do you do? ")
        print("")

        if action=="1":
            print("The only thing in this room is a stack of hay.\nThere is a locked door going forward again.")
        
        elif action=="2":
            print("your inventory contains: ")
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
            if useitem=="needle" and invlist[1]=="Needle":
                print("You try to pick the lock, only to realize that you don't know how to pick locks.\nThe disappointing quality of door-opening mechanisms here might become a recurring theme.")
                doorunlocked=True
                remove_item(invlist,"Needle",invwrite)
            else:
                print("You can't use your that here.")


        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
            if interact=="hay" or "haystack":
                print("You dig through the haystack and find a needle.\nIronic.")
                invapp.write("Needle")
            else:
                print("You can't interact with",interact)
        
        elif action=="5":
            move=input("Forward or back?")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.")
                    roomnum+=1
                    roomdone=True
                else:
                    print("The door is locked.")
            elif move=="back":
                print("The key you used to get in here broke, and the door closed behind you.\nIt seems like the only keyhole was on the other side of the door too, so there's no way to go back.")
            else:
                print("That wasn't an option.")
        else:
            print("Sorry, that wasn't an option.")

        print("")
        invapp.close()
        invread.close()
        invwrite.close()