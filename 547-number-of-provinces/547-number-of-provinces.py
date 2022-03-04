class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
            return 
        for row in range(len(isConnected)):
            if row not in visited:
                visited.add(row)
                dfs(row)
                count += 1
        return count