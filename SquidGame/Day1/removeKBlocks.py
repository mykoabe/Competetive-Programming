class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minW, currentCount, wCount = 100, 0, 0
        left = 0
        for i in range(len(blocks)):
            currentCount += 1
            wCount += blocks[i] == 'W'
            if currentCount == k:
                minW = min(minW, wCount)
                wCount -= blocks[left] == 'W'
                currentCount -= 1
                left += 1
        return minW


           
            
