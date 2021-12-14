def bubbleSorted(arr, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j + 1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSorted(arr, len(arr))
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
