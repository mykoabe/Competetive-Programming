from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        while arr:
            m = max(arr)
            i = arr.index(m)
            if i == 0:
                arr.reverse()
                res.append(m)
            elif i != len(arr) - 1:
                arr[0:i+1] = arr[0:i+1][::-1]
                res.append(i+1)
                arr.reverse()
                res.append(m)
            arr.remove(m)
        return res
sol = Solution()
print(sol.pancakeSort([3,2,4,1]))