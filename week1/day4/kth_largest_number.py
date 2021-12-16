from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        return str(nums[len(nums)-k])
sol = Solution()
print(sol.kthLargestNumber(["1","2","12","21"], 3))
