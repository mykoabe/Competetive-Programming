class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
         
            if dp[i]:
                return dp[i]
            
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])
            
            
        return min(dp[-2], dp[-1])