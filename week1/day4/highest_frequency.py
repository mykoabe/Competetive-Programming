from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, ops, answer = 0, 0, 1
        for high in range(1, len(nums)):
            if nums[high] != nums[high - 1]:
                ops += (high - low) * (nums[high] - nums[high - 1])
            while ops > k and low < high:
                ops -= (nums[high] - nums[low])
                low += 1
            answer = max(answer, high - low + 1)
        return answer


sol = Solution()
print(sol.maxFrequency([1, 2, 4], 5))
