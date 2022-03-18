class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = 0
        for i in range(k):
            leftSum += cardPoints[i]
       
        maxi = leftSum
        rightSum = 0
        n = len(cardPoints)
        
        for i in range(k):
            leftSum -= cardPoints[k - 1 - i]
            rightSum += cardPoints[n-1-i]
            maxi = max(maxi, leftSum + rightSum)
        return maxi
            
        
            