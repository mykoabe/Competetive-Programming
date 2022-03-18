class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for num in grid:
            for i in num:
                if i < 0:
                    count += 1
        return count