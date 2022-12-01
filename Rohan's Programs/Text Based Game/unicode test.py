def main():
    lanternlist=[0,0,0,0,0]
    displaylist=["\u25CB","\u25CB","\u25CB","\u25CB","\u25CB"]
    x=1
    print(*displaylist)
    while x==1:
        query=input("Which button will you press? (1, 2, 3, 4, 5, or exit): ")
        if query=="exit":
            x=0
        else:
            button=eval(query)
            if 1<=button<=5:
                button-=1
                lanternListEditor(button,lanternlist)
            else:
                print("Invalid input.")
        
        for i,e in enumerate(lanternlist):
            if e%2==0:
                displaylist[i]="\u25CB"
            else:
                displaylist[i]="\u25CF"
        print(*displaylist)
        if displaylist==["\u25CF","\u25CF","\u25CF","\u25CF","\u25CF"]:
            print("You hear the lock on the door click.")
            x=0
            doorunlocked=True

def lanternListEditor(lantern,list):
    if lantern==0:
        list[4]+=1
        list[0]+=1
        list[1]+=1
    elif lantern==4:
        list[3]+=1
        list[4]+=1
        list[0]+=1
    else:
        list[lantern-1]+=1
        list[lantern]+=1
        list[lantern+1]+=1
    return list

main()