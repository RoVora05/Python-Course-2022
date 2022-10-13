sentence=input("Enter your sentence: ")
splitsent=sentence.split(" ")
wordcount=len(splitsent)
print("There were",wordcount,"words in that sentence.")
lpw=0
for i in splitsent:
    lpw+=len(i)
print("On average, there were",lpw/wordcount,"per word.")