string1 = input()
words = string1.split()
words.sort()
newSentence=" ".join(words)
list1=[]
for i in words:
    if (i not in list1):
        list1.append(i)
for i in list1:
    print(i, end=" ")