#finds the unique characters in a string
Chars = {}
uniqueChars = []
string = str(input("enter a string: "))

for i in range(0,len(string)):
    if string[i] not in Chars:
        Chars[string[i]] = string.count(string[i])
    if Chars[string[i]] == 1:
        uniqueChars.append(string[i])

print(Chars)
print("Unique characters in the the string:",string, " are: ", uniqueChars)