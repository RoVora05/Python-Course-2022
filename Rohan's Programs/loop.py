def main():
    fun1(0)

def fun1(it):
    it+=1
    print("Iteration",it)
    fun1(it)


main()