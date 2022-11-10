from tbgcentral import *
def room1():
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
            print("There's nothing interesting in this room, just a desk with a key on it and a locked door going forward.\nI really hope you can put this together, or this might take a while.")
        
        elif action=="2":
            print("your inventory contains: ")
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
            if useitem=="key" and invlist[1]=="Key":
                print("The key fits into the door's lock, and immediately breaks.\nPoor quality key, but at least the door is open.")
                doorunlocked=True
                remove_item(invlist,"Key",invwrite)
            else:
                print("You can't use your that here.")


        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
            if interact=="key":
                print("You pick up the key.")
                invapp.write("Key")
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
                print("There's only one door in this room, and it goes forward.")
            else:
                print("That wasn't an option.")
        else:
            print("That wasn't an option.")

        print("")
        invapp.close()
        invread.close()
        invwrite.close()