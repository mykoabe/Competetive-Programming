from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        ans = []
        changed = sorted(changed)
        freq = Counter(changed)

        for num in changed:

            if freq[num] == 0:
                continue

            if freq[num*2] == 0:
                return []

            if num == 0 and freq[num] <= 1:
                return []

            ans.append(num)
            freq[num] -= 1
            freq[num*2] -= 1
        return ans


solution = Solution()
print(solution.findOriginalArray(
    [1, 3, 4, 2, 6, 8]))
