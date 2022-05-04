class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #O(1) space and O(n) time
        res = []
        # edge case
        if len(matrix) == 0:
            return res
        #col
        left, right = 0, len(matrix[0]) - 1 
        #row
        top, bottom = 0, len(matrix) - 1
        while left <= right and top <= bottom:
            
            for go_right in range(left, right + 1):
                res.append(matrix[top][go_right])
                
            for go_down in range(top + 1, bottom + 1):
                res.append(matrix[go_down][right])
                
            for go_left in (range(left, right))[::-1]:
                if top < bottom:
                    res.append(matrix[bottom][go_left])
            
            for go_up in (range(top + 1, bottom))[::-1]:
                if left < right:
                    res.append(matrix[go_up][left])
                
            left, right = left + 1, right - 1
            top, bottom = top + 1, bottom - 1
        return res
                
                

        
