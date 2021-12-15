def smallerNumbers(arr):
    count = 0
    lessNums = []
    for i in arr:
        for j in range(len(arr)):
            if(arr[j]-i < 0):
                count+=1
        lessNums.append(count)
        count = 0
    return lessNums
arr = [1,5,4,5,4,5,6]
print(smallerNumbers(arr))