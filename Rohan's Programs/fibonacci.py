import time
import math
def nFinder(nG,nC,p1,p2): # n Goal, n Current, previous number 1, previous number 2
    if nC==nG:
        return p1
    sum=p1+p2
    return nFinder(nG,nC+1,sum,p1)

def nFinderIt(n):
    p1,p2=0,1
    for i in range(n):
        p1,p2=p1+p2,p1
    return p1

def main():
    nG=int(input())
    s=time.time()
    print(nFinderIt(nG))
    print(time.time()-s)
    s=time.time()
    print(nFinder(nG,1,1,0))
    print(time.time()-s)
main()

