#finds if a pair of numbers in array equals a given sum
arr = [2,3,2,4,5,6,7,8,9]
sum = 4
pairs = {}
for i in range(0, len(arr)):
    temp = sum - arr[i]
    arr.pop(i)
    if temp in arr:
        print(True)
        break

