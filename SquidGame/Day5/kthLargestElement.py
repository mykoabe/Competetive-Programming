class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        # using Blum-Floyd-Pratt-Rivest-Tarjan algorithm (BFPRT) to find the kth largest
        # element in an array using O(n) time complexity and O(1) space complexity

        return self.helper(nums, 0, len(nums) - 1, k)
    def helper(self, nums, start, end, k):
        if start == end:
            return nums[start]
        pivot = self.partition(nums, start, end)
        if pivot == k - 1:
            return nums[pivot]
        elif pivot > k - 1:
            return self.helper(nums, start, pivot - 1, k)
        else:
            return self.helper(nums, pivot + 1, end, k)
         
    def partition(self, nums, start, end):
        pivot, index = nums[end], start
        for i in range(start, end):
            if nums[i] > pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[end] = nums[end], nums[index]
        return index

        # heap = []
        # for num in nums:
        #     heapq.heappush(heap,num)
        # while len(heap) > k:
        #     heapq.heappop(heap)            
        # return heap[0]
        