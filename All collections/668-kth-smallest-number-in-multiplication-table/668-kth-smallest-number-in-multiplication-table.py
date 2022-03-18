class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        m, n = min(m, n), max(m, n)
        low, high = 1, m * n
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for i in range(1, m+ 1):
                count += min(mid // i, n)
                if mid // i == 0 or count > k:
                    break
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low