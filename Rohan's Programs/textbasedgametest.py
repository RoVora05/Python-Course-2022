print("message")
options=["help","look around","pick lock"]
x=input("What do you do? ")

while x not in options:
    print("Invalid response. Type 'help' for a list of options.")
    x=input("What do you do? ")
if x=="help":
    print(options)