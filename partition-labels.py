class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {v: k for k, v in enumerate(s)}
        start, end = 0, 0
        ans = []
        
        for v, k in enumerate(s):
            
            end = max(end, d[k])
            if v == end:
                ans.append(v - start + 1)
                start = v + 1
                
        return ans
