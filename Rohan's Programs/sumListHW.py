def sumList(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum

def main():
    loops=eval(input("How many numbers in the list? "))
    list=[]
    for e in range(loops):
        number=eval(input("Enter an entry in the list: "))
        list.append(number)
    print(sumList(list))
main()