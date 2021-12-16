from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) // 3
        res = 0
        n = len(piles)
        while i < n:
            res += piles[i]
            i += 2
        return res


solution = Solution()
print(solution.maxCoins([2, 4, 1, 2, 7, 8]))
