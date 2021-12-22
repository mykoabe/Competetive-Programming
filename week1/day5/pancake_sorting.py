class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        tail = len(arr)
        ans = list()
        while True:
            imax = arr.index(max(arr[:tail]))
            if imax != tail - 1:
                if imax != 0: 
                    ans.append(imax + 1)
                    arr[:imax + 1] = arr[:imax + 1][::-1]
                ans.append(tail)
                arr[: tail] = arr[: tail][::-1]
            tail -= 1
            
            if tail == 0:
                #print(arr)
                return ans