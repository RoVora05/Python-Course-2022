def roomlogic(room):
    gameover=False
    print ("introduction stuff")
    options=["1. look around","2. check inventory","3. use item","4. interact with environment","5. move"]
    while gameover==False:
        print("You can:",options)
        action=input("What do you do? ")
        print("")

        if action=="1":
            print("room description")
        
        elif action=="2":
            print("your inventory contains",) # make an inventory.txt
        
        elif action=="3":
            useitem=input("Which item will you use? ")
        
        elif action=="4":
            interact=input("What would you like to interact with? ")
        
        elif action=="5":
            moveto=input("Which direction? ")
        
        else:
            print("Sorry, that wasn't an option.")
        
        print("")

roomlogic()

def intro():
    global name
    name=input("Please enter your name: ")
intro()