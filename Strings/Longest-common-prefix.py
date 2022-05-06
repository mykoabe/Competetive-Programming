class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #edge case
        if not strs:
            return ""
        strs.sort()
        res = ""
        for i in range(len(strs[0])):
            if i > len(strs[-1]) or strs[0][i] != strs[-1][i]:
                return res
            res += strs[0][i]
        return res
    # Time:  O(n * k), k is the length of the common prefix
    # Space: O(k)
        
            
        
