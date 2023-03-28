from random import *
def main():
    x=input()
    list=x.split("d")
    for i,e in enumerate(list):
        list[i]=int(e)
    answer=0
    for i in range(list[0]):
        answer+=randint(1,list[1])
    print(answer)
main()