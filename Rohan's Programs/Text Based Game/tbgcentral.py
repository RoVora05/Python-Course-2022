def intro():
    global name
    global file_location
    global options
    global roomnum
    roomnum=1
    options=["1. look around","2. check inventory","3. use item","4. interact with environment","5. move"]

    file_location="c:/Users/h4cke/Python Files Clone/Python-Class-Files/Rohan's Programs/Text Based Game/"
    name=input("Please enter your name: ")

    print("You wake up in your room in the dungeon.\nAgain.\nIt's probably time to leave this place.")

intro()

def roomlogic():
    gameover=False
    while gameover==False:
        if roomnum==1:
            roomnum=room1()

        elif roomnum==2:
            roomnum=room2()

        elif roomnum==3:
            roomnum=room3()

        elif roomnum==4:
            print("ENDING")

        else:
            print("Something went wrong.")

def remove_item(invlist,item,writer):
    invlist.remove(item)
    for i,e in invlist:
        if i!=len(invlist)-1:
            writer.write(e+'\n')
        else:
            writer.write(e)