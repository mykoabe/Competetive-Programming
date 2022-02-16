class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        p = 0
        for i in range (1, len(nums)):
            if nums[p] != nums[i]:
                nums[p + 1] = nums[i]
                p = p + 1
        return p + 1
    
        