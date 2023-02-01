class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        # prefix sum
        prefix = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] \
                - prefix[i][j] + mat[i][j]
        #print(prefix)
        res = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                r1, r2 = max(0, i-k), min(M, i+k+1)
                c1, c2 = max(0, j-k), min(N, j+k+1)
                res[i][j] = prefix[r2][c2] + prefix[r1][c1] \
                - (prefix[r1][c2] + prefix[r2][c1])
        return res
            
                
                
                
        
        