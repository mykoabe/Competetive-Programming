#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

def minimumAverage(customers):
    #time complexity O(nlogn)
    #space complexity O(n)
    # Write your code here
    waiting_time = 0 #the time where the ith person pizza is cooked
    total_time = 0  #this is the total time taken by the shefe to cook all of the pizza 
    customers.sort(reverse=True)
    heap = []
    while customers or heap:
        while customers and customers[-1][0] < total_time:
            heapq.heappush(heap, customers.pop()[::-1])
        if heap:
            task = heapq.heappop(heap)
            total_time += task[0]
            waiting_time += total_time - task[1]
            
        else:
            heapq.heappush(heap, customers.pop()[::-1])
            total_time = heap[0][1]
    return waiting_time // n
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
