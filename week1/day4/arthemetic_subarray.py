from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            n = len(arr)
            if n < 2:
                return False
            d = arr[1] - arr[0]
            for i in range(2, n):
                if arr[i]-arr[i-1] != d:
                    return False
            return True

        ans = []
        n = len(l)
        for idx in range(n):
            i, j = l[idx], r[idx]
            sub = nums[i:j+1]
            ans.append(check(sorted(sub)))

        return ans


solution = Solution()
print(solution.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7],
                                        [0, 0, 2],
                                        [2, 3, 5]))
