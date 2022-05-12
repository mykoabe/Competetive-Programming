class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #edge case
        if n == 0:
            return False
        
        if n & n-1 == 0:
            return True
        return False
    
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n == 0:
    #         return False
    #     if n == 1:
    #         return True
    #     return usingRecursion(n //2 )
    
    
    
    
    
        