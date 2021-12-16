from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # gives count of each element in arr and it returns a dictionary
        count = Counter(arr)
        sort = count.most_common()  # to sort on basis of count miko use most_common

        n = len(arr)
        half = n//2
        ans = 0
        # substract the highest count until the less than or equal to half
        for num in sort:
            if n <= half:
                break  # get out of the if close man
            n -= num[1]
            ans += 1
        return ans


sol = Solution()
print(sol.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
