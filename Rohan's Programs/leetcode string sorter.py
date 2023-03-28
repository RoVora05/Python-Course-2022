import random
def frequencySort(s):
    d={}
    for e in list(s):
        d[e]=0
        for e2 in list(s):
            if e==e2:
                d[e]+=1
    
    answer=""
    exclude=[]
    for e in d:
        i=0
        while i<len(s):
            if s[i] not in exclude:
                mostRecurring=s[i]
                break
            else:
                i+=1
        for key in d:
            if d[key]>d[mostRecurring] and key not in exclude:
                mostRecurring=key
        answer+=mostRecurring*d[mostRecurring]
        exclude.append(mostRecurring)

    print("\n"+answer+"\n")
    return answer



def main():
    x=input("Select which mode you would like to use:\n1. Input string\n2. Random string generation\n\n")
    if x=="1":
        while True: frequencySort(input("\nInput:\n"))
    elif x=="2":
        n=eval(input("Input # of letters:\n"))
        while True:
            string=""
            for i in range(n):
                string+=chr(random.randint(97,122))
            print(string)
            frequencySort(string)
main()
