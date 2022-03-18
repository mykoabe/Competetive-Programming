class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        low = self.lowest_position(nums, target)
        last = self.highest_position(nums, target) - 1
        
        if low == len(nums) or nums[low] != target:
            return [-1,-1]
        
        return [low,last]

    def lowest_position(self, nums, target):
        low = 0
        last = len(nums)

        while low < last:
            mid = (low + last) // 2
            if nums[mid] >= target:
                last = mid
            else:
                low = mid + 1
        return low
    
    def highest_position(self, nums, target):
        
        low = 0
        last = len(nums)
        while low < last:
            mid = (low + last) // 2
            if nums[mid] > target:
                last = mid
            else:
                low = mid + 1
        return low
    
 
