class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #let use bit masking/bloking
        res = 0
        bits = 32
        for i in range(bits):
            c = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    c += 1
            if c % 3 == 1:
                res |= mask
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res
        