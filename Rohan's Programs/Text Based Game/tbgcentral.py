def intro():
    global name
    global file_location
    global options
    options=["1. look around","2. check inventory","3. use item","4. interact with environment","5. move"]

    file_location="c:/Users/h4cke/Python Files Clone/Python-Class-Files/Rohan's Programs/Text Based Game/"
    name=input("Please enter your name: ")
    file=open(file_location+"room_descriptions.txt",'r')
    lines=file.readlines()

    print(lines[0])
intro()

def roomlogic():
    gameover=False
    while gameover==False:
        0
roomlogic()