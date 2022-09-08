def main():
    print ("This program calculates the future value of a 10 year investment.")
    principal=eval(input("Enter the initial principal: "))
    rate=eval(input("Enter the interest rate: "))
    period=eval(input("Enter the period: "))
    for i in range (10*period):
        principal*=(1+(rate))
    print("The value in",period, "years is", principal)
main()