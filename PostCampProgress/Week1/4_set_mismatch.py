# set mismatch brute force solution
# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return [nums[i], nums[i]+1]
        return [nums[-1], nums[-1]-1] if nums[-1] == n else [nums[-1], n] 

# I think I can use hashtable to improve the time complexity to O(n)
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                return [num, num+1]
            seen.add(num)
        return [nums[-1], nums[-1]-1] if nums[-1] == n else [nums[-1], n]

# using bit manipulation also reduces the space complexity to O(1) and time complexity to O(n)
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = 0
        for num in nums:
            xor ^= num
    # TODO: finish this
        

