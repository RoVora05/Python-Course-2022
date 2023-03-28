def generate(numRows):
    s=[[1]]
    for i in range(numRows-1):
        s.append([1])
    
    for i in range(1,numRows):
        for j in range(len(s[i-1])-1):
            s[i].append(s[i-1][j]+s[i-1][j+1])
        s[i].append(1)
    return s

def getRow(rowIndex):
    s=[[1]]
    for i in range(rowIndex):
        s.append([1])
    
    for i in range(1,rowIndex+1):
        for j in range(len(s[i-1])-1):
            s[i].append(s[i-1][j]+s[i-1][j+1])
        s[i].append(1)
    return s[rowIndex]

print(generate(eval(input("Input:\n"))))