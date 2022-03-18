class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        visit=set() # need to be visted
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    visit.add((r,c))
                elif grid[r][c]==1:
                    start = (r,c)
                elif grid[r][c]==2:
                    end= (r,c)
                    visit.add((r,c))
        
        def helper(r,c):
            
            if grid[r][c]==2 and len(visit)==0:
                return 1
            
            count = 0
            
            for v in [(r-1,c), (r+1,c), (r,c-1),(r,c+1)]: 
                if v in visit:
                    visit.remove(v)
                    count += helper(v[0], v[1])
                    visit.add(v) # for next path 
            return count

        return helper(start[0], start[1])
                
            
            