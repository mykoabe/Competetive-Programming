class Solution:
    def largestRectangleArea(self, heights):
        
        stack = []
        maxarea = 0
       
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                currentHeight = heights[stack.pop()]
                left = stack[-1] if stack else -1
                maxarea = max(maxarea, ((index - 1 - left) * currentHeight))
            stack.append(index)
            
            
        right = len(heights) - 1
        while stack and heights[stack[-1]] >= 0:
            currentHeight = heights[stack.pop()]
            left = stack[-1] if stack else -1
            maxarea = max(maxarea, ((right - left) * currentHeight))
        
        return maxarea
            
        