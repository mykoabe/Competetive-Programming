class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
        s_nums = sorted(nums)
        
        score = s_nums[-1] - s_nums[0]
        
        for x, y in zip(s_nums, s_nums[1:]):
            
            temp = max(s_nums[-1]-k, x + k) - min(s_nums[0]+k, y-k)
            score = min(score, temp)
        return score
