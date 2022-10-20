from tbgcentral import *
def room1():
    invread=open(file_location+"inventory.txt","r")
    invlist=invread.read().splitlines()
    invwrite=open(file_location+"inventory.txt","a")
    
    
    print("You can:",options)
    action=input("What do you do? ")
    print("")

    if action=="1":
        file=open(file_location+"room_descriptions")
        lines=file.readlines()
        print(lines[0])
    
    elif action=="2":
        print("your inventory contains: ")
        print(invlist)
    
    elif action=="3":
        useitem=input("Which item will you use? ")
        if useitem=="key" or useitem=="Key" and invlist[1]=="Key":
            invwrite.write("")
    
    elif action=="4":
        interact=input("What in the room would you like to interact with? ")
        if interact=="key" or "Key":
            print("You pick up the key.")
            invwrite.write("Key")
        else:
            print("You can't interact with",interact)
    
    elif action=="5":
        move=input("Forward or back? ")
    
    else:
        print("Sorry, that wasn't an option.")
    
    print("")
room1()