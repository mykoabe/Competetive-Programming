class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        count = 1
        
        temp_shoot = points[0][1]
        
        n=len(points)
        for i in range(1,n):
            if(points[i][0] <= temp_shoot):
                continue
            else:
                count = count + 1
                temp_shoot = points[i][1]
                
        return count
        
            
            
            
            