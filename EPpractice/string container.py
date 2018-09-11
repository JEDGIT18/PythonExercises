
orgstring  = input("Enter a string: ")
innerStr = input("What string do you wanna find in first string ")

temp = ""
innernum = 0
for i in range(0, len(orgstring)):
    if innerStr[innernum] == orgstring[i]:
        print("found")
        temp += orgstring[i]
        if temp == innerStr:
            print("True ", temp, " found.")
            break
        innernum += 1
        continue
    else:
        temp = ""
        innernum = 0

if temp != innerStr:
    print("not found ", False)


