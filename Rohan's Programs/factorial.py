import math
import time

def main():
    inp=int(input("Enter a number to take the factorial of:\n"))
    r=facRecursion(inp,1)
    print(r)
    b=math.factorial(inp)
    print(b)
    print(r==b)

def facRecursion(n,a):
    if n==0:
        return a
    return facRecursion(n-1,a*n)
main()