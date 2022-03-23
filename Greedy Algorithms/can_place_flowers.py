class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #greedy
        flowerbed = [0] + flowerbed + [0] #eg edge case [0] , 1
        #print(flowerbed)
        res = 0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                res += 1
                flowerbed[i] = 1
        return res >= n
