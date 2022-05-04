class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #simple tric
        for i, citation in enumerate(sorted(citations)):
            if len(citations) - i <= citation:
                return len(citations) - i
        return 0  #this becomes the edge case
      
      #also second tric
        
        # for i, citation in enumerate(sorted(citations, reverse=True)):
        #     if i >= citation:
        #         return i
        # return len(citations) #or I can return 0
        
