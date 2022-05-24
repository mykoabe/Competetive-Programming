class Solution:
    def compress(self, chars: List[str]) -> int:
        #["a","a","b","b","c","c","c"]
        n = len(chars) 
        cur = 0 
        i = 0
        while i < n:
            j = i
            while j < n - 1 and chars[j] == chars[j+1]: 
                j += 1
            chars[cur] = chars[i] 
            cur += 1
            if i != j:
                times = str(j-i+1)  
                tLen = len(times)
                for k in range(tLen):
                    chars[cur+k] = times[k]
                cur += tLen
            i = j + 1 
        return cur
        
        
