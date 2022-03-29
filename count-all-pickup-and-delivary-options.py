class Solution:
    def countOrders(self, n: int) -> int:
        start = 1
        ans = 1
        for i in range(1, n):
            start += 2
            ans *= start
                        
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return (ans * fact) % (10**9 + 7)
