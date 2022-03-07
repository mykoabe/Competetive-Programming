class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        self.count =0
        
        def dfs(i,j):
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            if i<0 or i > len(grid)-1 or j<0 or j> len(grid[0])-1:
                return self.count
            if grid[i][j] == '#':
                return self.count
            if grid[i][j] == 0:
                return self.count
            grid[i][j] ='#'
            self.count -= 1
            for d in directions:
                dfs(i+d[0], j+d[1])
            return self.count
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
                        self.count+=1
        r = len(grid)
        c = len(grid[0])
        for j in range(c):
            if grid[0][j] == 1:
                dfs(0,j)
        for i in range(1,r-1):
            if grid[i][0] == 1:
                # self.count-=1
                dfs(i,0)
        for j in range(c):
            if grid[r-1][j] == 1:
                # self.count-=1
                dfs(r-1,j)
        for i in range(1,r-1):
            if grid[i][c-1] == 1:
                # self.count-=1
                dfs(i,c-1)
        return self.count