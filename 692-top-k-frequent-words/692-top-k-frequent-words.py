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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        pq = list()
        for word, count in counter.items():
            heapq.heappush(pq, WordFreq(count=count, word=word))
            if len(pq) > k:
                heapq.heappop(pq)
        result = list()
        while pq:
            wf = heapq.heappop(pq)
            result.append(wf.word)
            
        return result[::-1]