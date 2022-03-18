class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height)-1
        area = 0
        count = 0
        while count<j:
            area = max(area,(j-count)*min(height[count],height[j]))    
            right = height[j]
            left = height[count]
            if right<left:
                j-=1
            else:
                count+=1
        return area
        
