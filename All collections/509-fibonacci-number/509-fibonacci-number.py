class Solution:
    def fib(self, n: int) -> int:
        
        dp = [0 for _ in range(n + 1)]
        if n == 0:
            dp[n] = 0
            return dp[n]
        
        if n == 1:
            dp[n] = 1
            return dp[n]
        
        if dp[n]: return dp[n]
        
        dp[n] = self.fib(n-1) + self.fib(n - 2)
        return dp[n]
     