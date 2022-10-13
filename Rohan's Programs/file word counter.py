file_location=input("Enter the file location: ")
file=open(file_location)
wordcount=0
cpw=0
lines=file.readlines()
for i in lines:
    splitsent=i.split(" ")
    wordcount+=len(splitsent)
    for e in splitsent:
        cpw+=len(e)
print("The file contains",wordcount,"words.")
print("There are",len(lines),"lines, with an average of",wordcount/len(lines),"words per line.")
print("There is an average of",cpw/wordcount,"characters per word.")