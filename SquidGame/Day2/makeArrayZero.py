class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                numsDict[nums[i]] = numsDict.get(nums[i], 0) + 1
        #print(numsDict)
        return len(numsDict)
