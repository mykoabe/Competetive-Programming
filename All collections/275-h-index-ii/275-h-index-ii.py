class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations) - 1
        res = 0
        while low <= high:
            mid = (low + high) // 2
            h = len(citations) - mid
            if citations[mid] >= h:
                res = h
                high = mid - 1
            else:
                low = mid + 1
        return res