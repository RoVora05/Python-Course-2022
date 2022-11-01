def convert(input):
    returnlist=[]
    for i in input:
        returnlist.append(int(i))
    return returnlist

def main():
    list1=[1,2,3,4,12]
    x=convert(list1)
    print(type(x[0]))
main()