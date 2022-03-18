#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    heapq.heapify(A)
    operation = 0
    while True:
        firstMin = heapq.heappop(A)
        if firstMin >= k:
            return operation
        if A:
            secondMin = heapq.heappop(A)
            number = firstMin + 2 * secondMin
            heapq.heappush(A, number)
            operation += 1
        else:
            return -1
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
