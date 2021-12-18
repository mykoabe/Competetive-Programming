class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False 
        b = s[:]
        vals = ['()','[]','{}']
        while True:
            if len(b) == 0:
                return True
            elif vals[0] in b:
                b = b.replace(vals[0],'')
                print(vals[0], b)
            elif vals[1] in b:
                b = b.replace(vals[1],'')
            elif vals[2] in b:
                b = b.replace(vals[2],'') 
            else: return False
sol = Solution()
print(sol.isValid("(){}"))