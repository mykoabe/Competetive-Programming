class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height)-1
        area = 0
        i = 0
        while i<j:
            area = max(area,(j-i)*min(height[i],height[j]))    
            right = height[j]
            left = height[i]
            if right<left:
                j-=1
            else:
                i+=1
        return area
        