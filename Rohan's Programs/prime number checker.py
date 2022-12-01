num=input("Enter the number: ")
numlist=list(num)
if numlist==numlist[::-1]:
    print(True)
else:
    print(False)