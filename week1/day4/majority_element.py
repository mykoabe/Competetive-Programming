from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first = 0
        second = 1
        count1 = 0
        count2 = 0

        for n in nums:
            if first == n:
                count1 += 1
            elif second == n:
                count2 += 1
            elif count1 == 0:
                first, count1 = n, 1
            elif count2 == 0:
                second, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (first, second) if nums.count(n) > len(nums)//3]
