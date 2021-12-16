from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                count += 1
                i += 1
                j -= 1
            elif s < k:
                i += 1
            else:
                j -= 1
        return count


solution = Solution()
print(solution.maxOperations([1, 2, 3, 4], 5))
