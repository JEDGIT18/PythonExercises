word = input("Enter a string: ")
vowels =['a','e','i','o','u']
vowelsInWord =[]
for i in range(0, len(word)):
    if word[i].lower() in vowels:
        print(word[i])
        vowelsInWord.append(word[i])

newWord = ""
for i in range(0, len(word)):
    if word[i] in vowels:
        newWord += vowelsInWord[len(vowelsInWord) - 1]
        vowelsInWord = vowelsInWord[:-1]
    else:
        newWord += word[i]


print(newWord)
