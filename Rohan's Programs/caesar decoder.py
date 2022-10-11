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
decode()

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
encode()