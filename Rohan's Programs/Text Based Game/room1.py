from tbgcentral import *
def room1():
    invread=open(file_location+"inventory.txt","r")
    invlist=invread.read().splitlines()
    invwrite=open(file_location+"inventory.txt","a")
    file=open(file_location+"room_descriptions")
    lines=file.readlines()
    roomdone=False
    while roomdone==False:
        doorunlocked=True
        print("You can:",options)
        action=input("What do you do? ")
        print("")

        if action=="1":
            file=open(file_location+"room_descriptions")
            lines=file.readlines()
            print(lines[1])
        
        elif action=="2":
            print("your inventory contains: ")
            print(invlist)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
            if useitem=="key" and invlist[1]=="Key":
                print("You unlock the door.")
        
        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
            if interact=="key":
                print("You pick up the key.")
                invwrite.write("Key")
            else:
                print("You can't interact with",interact)
        
        elif action=="5":
            move=input("Forward or back?")
            if move=="forward":
                if doorunlocked==True:
                    print("You move into the room in front of you.")
                    roomdone=True
                else:
                    print("The door is locked.")
            elif move=="back":
                print("There's only one door in this room, going forward.")
            else:
                print("That wasn't an option.")
        else:
            print("Sorry, that wasn't an option.")
        
        print("")
room1()