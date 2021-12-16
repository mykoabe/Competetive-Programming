from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        begin = intervals[0][0]
        end = intervals[0][1]
        merge_pointer = 0
        
        for i in range(1, len(intervals)):
            if(intervals[i][0] <= end):
                end = max(end, intervals[i][1])
            else:
                intervals[merge_pointer] = [begin, end]
                merge_pointer += 1
                begin = intervals[i][0]
                end = intervals[i][1]
                
        intervals[merge_pointer] = [begin, end]
        merge_pointer += 1     
        return intervals[:merge_pointer]
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))