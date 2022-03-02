class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
       

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(image, r, c, newColor, color):
            if  (0 <= r < len(image) and \
                 0 <= c < len(image[0]) and \
                    image[r][c] == color):
                for d in directions:
                    dfs(image, r+d[0], c+d[1], newColor, color)
                    image[r][c] = newColor
            else:
                return 
        color = image[sr][sc]
        if color == newColor: return image
        dfs(image, sr, sc, newColor, color)
        return image