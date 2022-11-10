from calendar import c


def decode():
    print("Enter your code.")
    print("(Only use capital letters and spaces)")
    code=input()
    final=""
    character_list=list(code)
    for i in character_list:
        char=ord(i)
        if char==32:
            char-=3
        elif char>=88:
            char-=26
        char+=3
        final+=chr(char)
    print(final)
    print("")

def encode():
    print("Enter your phrase.")
    print("(Only use capital letters and spaces)")
    code=input()
    final=""
    character_list=list(code)
    for i in character_list:
        char=ord(i)
        if char==32:
            char+=3
        elif char<=67:
            char+=26
        char-=3
        final+=chr(char)
    print(final)
    print("")

def main():
    x=0
    while x==0:
        query=input("Would you like to encode, decode, or exit? (c/d/e): ")
        if query=="c":
            print("")
            encode()
        elif query=="d":
            print("")
            decode()
        elif query=="e":
            x=1
        else:
            print("Invalid Response")

if __name__=="__main__":
    main()