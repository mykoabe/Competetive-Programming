class Solution:
    def largestNumber(self, nums):
        snums = [str(num) for num in nums]
        self.quick_sort(0, len(snums)-1, snums)
        tmp = ''.join(snums).lstrip('0')
        return tmp if tmp else '0'

    def quick_sort(self, left, right, nums):
        if left > right:
            return
        pivot, start, end = left, left, right
        while left < right:
            while left < right and nums[right]+nums[pivot] <= nums[pivot]+nums[right]:
                right -= 1
            while left < right and nums[left]+nums[pivot] >= nums[pivot]+nums[left]:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        if left == right:
            nums[pivot], nums[left] = nums[left], nums[pivot]
        self.quick_sort(start, left-1, nums)
        self.quick_sort(left+1, end, nums)
