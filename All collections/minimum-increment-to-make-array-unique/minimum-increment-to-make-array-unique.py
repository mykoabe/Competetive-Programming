class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        nums.sort()
        temp = nums[0]
        
        for x in nums:
            if x > temp:
                temp = x + 1
            else:
                count += temp - x
                temp += 1
        return count

        