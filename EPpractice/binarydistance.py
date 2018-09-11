#Converts a number to binary and finds its binary gap
check = False
while not check :
    try:
        num = int(input("Input a number: 0 - 255 "))
        check = True
    except ValueError:
        print("Enter a number!")

binaryStr = ""
max = 128
while num > 1 or len(binaryStr) != 8:
    if num >= max:
        num -= max
        max /= 2
        binaryStr += "1"
    else:
        print(binaryStr)
        binaryStr += "0"
        max /= 2

#  use   bin(num)[2:] to create string
maxDist = 0
innernum = 0
for i in range(0, len(binaryStr)):
    if binaryStr[i] == "0":
        innernum += 1
        if innernum >= maxDist:
            maxDist = innernum
        continue
    else:
        temp = ""
        innernum = 0

print(binaryStr)
print("Largest Binary gap is: ", maxDist)

