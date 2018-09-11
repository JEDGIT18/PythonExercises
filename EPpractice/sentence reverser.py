orgstring  = input("Enter a sentance: ")

sentence = []
temp = ""
for i in range(0, len(orgstring)):
    temp += orgstring[i]
    if orgstring[i] == " ":
        sentence.append(temp)
        temp = ""
print(sentence)
newSentence = ""
for i in range(len(sentence),0, -1):
    newSentence += sentence[i - 1]

print("Orignal sentence ", orgstring)
print(newSentence)