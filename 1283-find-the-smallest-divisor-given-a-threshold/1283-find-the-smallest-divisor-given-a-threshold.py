class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            res = sum(ceil(num / mid) for num in nums)
            if res > threshold:
                low = mid + 1
            else:
                high = mid - 1             
        return low