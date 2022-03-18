class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # O(nk) solution
       #we can use this shorthand[for head in matrix for i in head [:k]]
        heap = []
        for head in matrix:   #o(n)
            #o(k)
            for i in head:
                heapq.heappush(heap, i)
                
        while heap and k > 1: # O(k)
            heapq.heappop(heap) # O(logk)
            k-=1 
        
        return heap[0]
       