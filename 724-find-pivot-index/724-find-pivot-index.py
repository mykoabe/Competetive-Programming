class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #using prefix sum
        rightSum = []
        leftSum = []
        for i in range(len(nums)):
            if i:
                leftSum.append(leftSum[i-1] + nums[i])
                rightSum.append(rightSum[i-1] + nums[len(nums) - 1 - i])
            else:
                leftSum.append(nums[i])
                rightSum.append(nums[len(nums) - 1])
        for i in range(len(nums)):
            if (leftSum[i] == rightSum[len(nums)-1 - i]):
                return i
        return -1
    