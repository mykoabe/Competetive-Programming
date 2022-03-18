class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return [x[0] for x in Counter(nums).most_common(k)] simplest solution
        #solution using heap
        counter = Counter(nums)
        heap = []
        
        for num, count in counter.items():
            heappush(heap, (num, count))
        
        result = []
        for w in nlargest(k, heap, key=lambda x: x[1]):
            result.append(w[0])
        return result
        