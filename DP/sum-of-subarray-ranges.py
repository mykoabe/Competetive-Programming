class Solution:
    def subArrayRanges(self, nums):
        
        #optimized dp solution but time limit exceded dude 
#         n = len(nums)
#         dp = [[(0, 0) for i in range(n)] for j in range(n)]
#         dp[n-1][n-1] = (nums[n-1], nums[n-1])

#         res = 0
#         for i in range(n-2, -1, -1):
#             for j in range(i, n):
#                 if dp[i][j-1] != (0, 0):
#                     dp[i][j] = (max(dp[i][j-1][0], nums[j]), min(dp[i][j-1][1], nums[j]))

#                 elif dp[i + 1][j] != (0,0):
#                     dp[i][j] = (max(dp[i + 1][j][0], nums[i]), min(dp[i + 1][j]                                              [1],nums[i]))
#                 else:
#                     dp[i][j] = (nums[i], nums[j])
#                 res += dp[i][j][0] - dp[i][j][1]
#         return res
        
        #brute force solution
        n = len(nums)
        count = 0
        for i in range(n):
            curMin = float('inf')
            curMax = -float('inf')
            for j in range(i, n):
                curMin = min(curMin, nums[j])
                curMax = max(curMax, nums[j])
                count += curMax - curMin
        return count
        
