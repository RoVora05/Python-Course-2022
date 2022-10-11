def intro():
    global name
    global file_location
    global room
    room=1
    file_location="c:/Users/h4cke/Python Files Clone/Python-Class-Files/Rohan's Programs/Text Based Game/"
    name=input("Please enter your name: ")
    file=open(file_location+"playerdata.txt",'w')
    file.write(name)
    print("Intro text")
intro()

def roomlogic():
    gameover=False
    options=["1. look around","2. check inventory","3. use item","4. interact with environment","5. move"]
    while gameover==False:
        print("You can:",options)
        action=input("What do you do? ")
        print("")

        if action=="1":
            file=open(file_location+"room_descriptions")
            lines=file.readlines()
            print(lines[room])
        
        elif action=="2":
            print("your inventory contains: ")
            file=open(file_location+"inventory.txt",'r')
            lines=file.read().splitlines()
            print(lines)
        
        elif action=="3":
            useitem=input("Which item will you use? ")
        
        elif action=="4":
            interact=input("What in the room would you like to interact with? ")
        
        elif action=="5":
            move=input("Forward or back? ")
        
        else:
            print("Sorry, that wasn't an option.")
        
        print("")

roomlogic()