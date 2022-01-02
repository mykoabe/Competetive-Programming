class Solution:
     def longestSubarray(self, nums, limit):
            
        maxq = deque()
        minq = deque()
        
        i = 0
        for elem in nums:
            
            while(len(maxq) > 0 and elem > maxq[-1]):
                maxq.pop()
                
            maxq.append(elem)
            
            while(len(minq) > 0 and elem < minq[-1]):
                minq.pop()
                
            minq.append(elem)
            
            if abs(maxq[0] - minq[0]) > limit:
                if nums[i] == maxq[0]:
                    maxq.popleft()
                elif nums[i] == minq[0]:
                    minq.popleft()
                    
                i+=1
                
        return len(nums) - i