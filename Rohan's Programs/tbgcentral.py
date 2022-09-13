def main():
    gameover=False
    room=1
    name=input("Please enter your name: ")
    print ("introduction stuff")
    inventory=["compass"]
    options=["1. look around","2. check inventory","3. use item","4. interact with environment","5. move"]
    while gameover==1:
        print("You can:",options)
        action=input("What do you do? ")
        print("")

        if action=="1":
            print("room description")
        
        elif action=="2":
            print("your inventory contains",inventory)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
        
        elif action=="4":
            interact=input("What would you like to interact with? ")
        
        elif action=="5":
            moveto=input("Which direction? ")
        
        else:
            print("Sorry, that wasn't an option.")
        
        print("")

        

main()