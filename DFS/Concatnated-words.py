class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        res = []
        wordSet = set(words)       
        def dfs(word):
            if word in wordSet:
                return True
            for i in range(1, len(word)):
                if word[:i] in wordSet and dfs(word[i:]):
                    return True
            return False
        
        for word in words:
            wordSet.remove(word) 
            if dfs(word):
                res.append(word)
            wordSet.add(word) 
        return res

    
                        
