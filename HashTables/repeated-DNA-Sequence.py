class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
     
        repeated = set()
        seen = set()
        for i in range(len(s)):
            cur = s[i : i+ 10]
            if cur in seen:
                repeated.add(cur)
            else:
                seen.add(cur)
        return list(repeated)
    
    # using sliding window I gonna do it later
