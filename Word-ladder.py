class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        q = collections.deque([(beginWord, 1)])
        while q:
            word, length = q.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    created = word[:i] + char + word[i+1:]
                    if created in wordSet and created != word:
                        wordSet.remove(created)
                        q.append((created, length + 1))
        return 0
        
       
        
        
