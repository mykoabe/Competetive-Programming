class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
      
        if len(num) <= k:
            return "0"
        
        stack = []
        
      
        for i, number in enumerate(num):
            number = int(number)
            
            while k != 0 and stack and stack[-1] > number:
                stack.pop()
                k -= 1
            stack.append(number)
                
        res = ""
    
        for entry in stack:
               res += str(entry) 
        
        if k != 0:
            res = res[:-k]
        res = str(int(res))
        
        return res
        