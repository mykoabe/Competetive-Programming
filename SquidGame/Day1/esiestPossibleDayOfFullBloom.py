class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantGrow = sorted(zip(plantTime,growTime), key=lambda x:-x[1])
        start, final = plantGrow[0][0], sum(plantGrow[0])
        for i in range(1, len(plantGrow)):
            plantT, growT = plantGrow[i]
            start += plantT
            final = max(start + growT, final)
        return final