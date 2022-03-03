class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    q.append((i,j,0))
        seen = set()
        while q:
            y, x, d = q.popleft()
            dirs = {(y-1,x),(y+1,x),(y,x+1),(y,x-1)}
            for y1,x1 in dirs:
                if 0 <= y1 < n and 0 <= x1 < m and (y1, x1) not in seen and grid[y1][x1] == 1:
                    seen.add((y1,x1))
                    count -= 1
                    if count == 0:
                        return d+1
                    q.append((y1, x1, d+1))
        return 0 if count == 0 else -1
            