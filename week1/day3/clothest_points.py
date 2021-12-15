from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # just keep calm and do miko🤾 time complextiy high dude
        distance = []
        for p in points:
            x = math.sqrt(p[0]**2 + p[1]**2)
            # create tuple of distance and coordinate
            distance.append((x, p))
        for i in range(len(distance)):
            min = i
            for j in range(i+1, len(distance)):
                if(distance[min] > distance[j]):
                    min = j
            distance[min], distance[i] = distance[i], distance[min]
        return [x[1] for x in distance[:k]]
