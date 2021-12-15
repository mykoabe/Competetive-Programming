from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            min = i
            for j in range(i+1, len(nums)):
                if(nums[min] > nums[j]): 
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
            if(nums[i] == target):
                res.append(i)
        return res
sol = Solution()
nums = [2,3,4,5,3,1,2]
target = 2
print(sol.targetIndices(nums, target))
