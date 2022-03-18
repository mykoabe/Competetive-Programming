class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [0 for _ in range(len(prices) + 1)]
    
        for i in range(1,len(prices)):
            if dp[i]:
                return dp[i]
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
        return max(dp)