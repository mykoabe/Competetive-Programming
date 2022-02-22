class WordFreq:
    def __init__(self, word, count):
        self.word = word
        self.count = count
        
    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count == other.count:
            return other.word < self.word 
        return False
    
    
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = []
        for word, count in counter.items():
            heapq.heappush(heap, WordFreq(count=count, word=word))
     
            
        result = ""
        while heap:
            wf = heapq.heappop(heap)
            result+=wf.word * wf.count
            
        return result[::-1]
        
