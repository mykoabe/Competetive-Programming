class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        def binarySearch(row):
            low, high = 0, n-1
            
            while low <= high:
                mid = low + (high-low) // 2
                left = -1 if mid == 0 else mat[row][mid-1]
                right = -1 if mid == n-1 else mat[row][mid+1]
                top = -1 if row == 0 else mat[row-1][mid]
                bottom = -1 if row == m-1 else mat[row+1][mid]
                
                if left < mat[row][mid] > right and top < mat[row][mid] > bottom: 
                    return mid
                if left >= right:
                    high = mid - 1
                else: low = mid + 1
                    
            return None
        
        for row in range(m):
            col = binarySearch(row)
            if col is not None: return [row, col]
                
        return []
            