class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # O(1) is become O(logn) but as n is 32 bit integer time and O(1) space
        
        def dfs(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        return dfs(k-1) % 2
    
        
        
