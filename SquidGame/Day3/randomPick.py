class Solution:
    
        def __init__(self, w: List[int]):
            self.w = w
            self.prefix_sum = [0]
            for i in range(len(w)):
                self.prefix_sum.append(self.prefix_sum[-1] + w[i])
            self.total_sum = self.prefix_sum[-1]
            
        def pickIndex(self) -> int:
            target = self.total_sum * random.random()
            left, right = 0, len(self.w)
            while left < right:
                mid = (left + right) // 2
                if target > self.prefix_sum[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left - 1