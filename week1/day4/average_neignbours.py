from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n-1):
            previousElement = nums[i-1]
            currentElement = nums[i]
            nextElement = nums[i+1]
            if (previousElement < currentElement < nextElement) or (previousElement > currentElement > nextElement):
                nums[i+1], nums[i] = nums[i], nums[i+1]
        return nums
sol = Solution()
print(sol.rearrangeArray([1, 2, 3, 4, 5]))
