from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sort = count.most_common(k)
        return [res for res, _ in sort]
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))