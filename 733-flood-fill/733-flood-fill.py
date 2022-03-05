class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        
        m = len(image)
        n = len(image[0])
        
        def dfs(image, r, c, newColor, oldColor):
            #old color is the color at image[sr][sc]
            
            if (0 <= r < len(image) ) and (0 <= c < len(image[0])) and image[r][c] == oldColor:
                
                for d in directions:
                    dfs(image, r+d[0], c+d[1], newColor, oldColor)
                    image[r][c] = newColor
            else:
                return 
            
        oldColor = image[sr][sc]
        if oldColor == newColor: return image 
        dfs(image, sr, sc, newColor, oldColor)
        return image
        
            
                
                
            
        