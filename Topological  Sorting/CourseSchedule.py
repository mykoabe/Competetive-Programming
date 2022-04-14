class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        dependency = defaultdict(list)
        q = deque()
        
        for c1,c2 in prerequisites:
            indegree[c1] += 1
            dependency[c2].append(c1)
            
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            course = q.popleft()
            
            for c in dependency[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
                    
        return max(indegree) == 0