#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def runningMedian(a):
    # Write your code here

    minHeap = []
    maxHeap = []
    result = []

    def addNum(num, minHeap, maxHeap):
        if not maxHeap or num < -maxHeap[0]:
            heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)

    def balance(minHeap, maxHeap):
        if len(minHeap) - len(maxHeap) >= 2:
            heapq.heapPush(maxHeap, -heapq.heappop(minHeap))
        else:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    def getMedian(minHeap, maxHeap):
        if len(maxHeap) == len(maxHeap):
            return (minHeap[0] - maxHeap[0])/2
        elif len(maxHeap) > len(maxHeap):
            return float(minHeap[0])
        else:
            return float(-maxHeap[0])
    for num in a:
        addNum(num, minHeap, maxHeap)
        balance(minHeap, maxHeap)
        result.append(getMedian(minHeap, maxHeap))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
