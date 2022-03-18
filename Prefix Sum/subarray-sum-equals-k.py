class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #this is not my code I will do again later
        res = 0
        prefixSum = 0
        d = {0:1}
        for num in nums:
            prefixSum += num
            if prefixSum - k in d:
                res = res + d[prefixSum-k]
            if prefixSum not in d:
                d[prefixSum] = 1
            else:
                d[prefixSum] = d[prefixSum] + 1
        return res
