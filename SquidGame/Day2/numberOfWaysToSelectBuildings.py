class Solution:
    def numberOfWays(self, s: str) -> int:
        # using prefix sum
        prefix_sum = [int(i) for i in accumulate([int(j) for j in s])]    
        n, res = len(s), 0    
        res = 0
        for i in range(1, n-1):
            start, end = prefix_sum[i-1], prefix_sum[n-1] - prefix_sum[i]
            if s[i] == '0':
                res += (start) * (end)
            else:
                res += (i - start) * abs((n - i) - end - 1)
            
        return res
    
        # number of zeros, ones, zeroOnes and oneZeros
        # _0, _1, _01, _10, res = 0, 0, 0, 0, 0
        # for b in s:
        #     if b == '0':
        #         _0 += 1
        #         _10 += _1
        #         res += _01
        #     else:
        #         _1 += 1
        #         _01 += _0
        #         res += _10 
        # return res