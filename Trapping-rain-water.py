class Solution:
    def trap(self, height: List[int]) -> int:
        #edge case
        if not height:
            return 0
        
        l_max = r_max = total_water = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                if height[left] < l_max:
                    total_water += l_max - height[left]
                else:
                    l_max = height[left]
                left += 1
            else:
                if height[right] < r_max:
                    total_water += r_max - height[right]
                else:
                    r_max = height[right]
                right -= 1
        return total_water
            
                
        
        
        
        
