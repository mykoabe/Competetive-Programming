class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        count = 0
        heap = []
        for i in range(1, len(heights)):
            change = heights[i] - heights[i-1]
            if change > 0:
                heapq.heappush(heap, change)
                if ladders == 0:
                    bricks -= heapq.heappop(heap)
                else:
                    ladders -= 1
                if bricks < 0:
                    return i - 1
        return len(heights)-1
            
                