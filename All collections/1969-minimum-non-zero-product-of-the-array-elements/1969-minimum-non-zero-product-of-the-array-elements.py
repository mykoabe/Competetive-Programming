class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(2, p, mod) - 1) * pow(pow(2, p, mod) - 2, pow(2, p - 1) - 1, mod) % mod
        