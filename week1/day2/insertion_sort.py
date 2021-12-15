#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for n in range(1,n):
        i = arr[n]
        while n>0:
            if i > arr[n-1]:
                arr[n] = i
                print(*arr)
                break
            else:
                arr[n] =arr[n-1]
            n-=1
        else:
            arr[0] = i
            print(*arr)
        


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)