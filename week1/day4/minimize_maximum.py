from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        i = 0
        j = len(nums)-1
        for inx in range(j+1):
            res.append(nums[i]+nums[j])
            i += 1
            j -= 1
        return max(res)


sol = Solution()
print(sol.minPairSum(
    [3, 5, 2, 3]))
