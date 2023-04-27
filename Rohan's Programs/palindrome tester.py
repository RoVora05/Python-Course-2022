import time
def iterativeTester(string):
    sL=list(string)
    reversedString=""
    for i in range(len(sL)):
        reversedString+=sL.pop(-1)
    if string==reversedString:return True
    return False


def whileTester(string,l,r):
    while True:
        if l>=r: return True
        elif string[l]==string[r]:
            l+=1
            r-=1
        else:return False

def recursiveTester(string,l,r):
    if l>=r:
        return True
    elif string[l]==string[r]:
        return recursiveTester(string,l+1,r-1)
    return False

def main():
    phrase=input("Enter phrase:\n")
    s=time.time()
    print(str(iterativeTester(phrase))+",",time.time()-s)
    s=time.time()
    print(str(whileTester(phrase,0,len(phrase)-1))+",",time.time()-s)
    s=time.time()
    print(str(recursiveTester(phrase,0,len(phrase)-1))+",",time.time()-s)
main()