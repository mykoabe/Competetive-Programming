class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        def condition(x): 
            res = 0
            for i in inventory:
                if i > x:
                    res += i - x
            return res
        left, right = 0, inventory[0]
        while left < right:
            mid = (left + right + 1) // 2
            if condition(mid) > orders:
                left = mid
            else:
                right = mid - 1
        res = 0
        for i in inventory:
            if i > left:
                res += (i + left + 1) * (i - left) // 2
                orders -= i - left
        res += orders * (left + 1)
        return res % (10 ** 9 + 7)


        # heap solution
        # heap = [-i for i in inventory]
        # heapq.heapify(heap)
        # res = 0
        # while orders:
        #     cur = heapq.heappop(heap)
        #     res += -cur
        #     heapq.heappush(heap, cur + 1)
        #     orders -= 1
        # return res % (10 ** 9 + 7)
        

# time complexity: O(nlogn)
# space complexity: O(1)
        
