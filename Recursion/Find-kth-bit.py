class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s0 = '0'
        for i in range(1, n+1):
            rev_str = self.inverse_reverse(s0)
            s0 = s0 + '1' + rev_str
            rev_str = s0
        return s0[k-1]
    def inverse_reverse(self, s):
        ans = ''
        for i in range(len(s)):
            if s[i] == '0':
                ans += '1'
            elif s[i] == '1':
                ans += '1'
                
        return ans[::-1]
        
                
            
        
