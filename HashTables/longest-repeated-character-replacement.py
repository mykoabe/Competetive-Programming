class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #time O(n) space O(1)
        
        res = 0
        counts = [0] * 26
        times, i, j = k, 0, 0
        
        while j < len(s):
            
            counts[ord(s[j]) - ord('A')] += 1
            if s[j] != s[i]:
                times -= 1
                if times < 0:
                    res = max(res, j - i)
                    while i < j and times < 0:
                        
                        counts[ord(s[i]) - ord('A')] -= 1
                        i += 1
                        times = k - (j - i + 1 - counts[ord(s[i]) - ord('A')])
            j += 1
            
        return max(res, j - i + min(i, times))
    
    #using sliding window -> no hasab dude
    
