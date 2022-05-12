import collections
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        graph = collections.defaultdict(list)
        q = collections.deque()
        
        for u,v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        path = []  
        while q:
            i = q.popleft()
            path.append(i)
            for c in graph[i]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)   
        return path if len(path) == numCourses else []


        


    
        
          
           
           
          
                
      