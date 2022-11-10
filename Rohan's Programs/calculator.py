def main():
    expr=0
    print("Welcome! Type '12321' when you are done.")
    while expr!=12321:
        expr=eval(input("Enter your expression to calculate: "))
        print("The answer is",expr)
    print("See you later!")
main()