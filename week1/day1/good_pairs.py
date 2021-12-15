class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numGoodPairs = 0
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums)-i-1):
                if(i == j):
                    continue
                if(nums[i] == nums[j]):
                    numGoodPairs = numGoodPairs + 1
        return numGoodPairs
sol = Solution()
arr = [1,1,1,1]
print(sol.numIdenticalPairs(arr))
