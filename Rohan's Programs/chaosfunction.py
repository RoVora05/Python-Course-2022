def main():
    print("This program illustrates a chaotic function")
    a = 0
    b = 0
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n=eval(input("How many numbers should I print?"))
    for i in range(n):
        x = 3.9 * (x - x * x)
        y = 4.5 * (y - y * y)
        print(str(round(x,5)) + " " + str(round(y,5)))
        a = a + x
        b += y
    print("The first average is "+str(a/n)+ " and the second average is "+ str(b/n))
main()