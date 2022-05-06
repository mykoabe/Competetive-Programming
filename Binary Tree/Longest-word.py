class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        
        #insert every word letter by letter to the trie
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isEnd = True
        
        res = ''
        for word in words:            
            if len(word) < len(res):
                continue         
            cur = root
            for letter in word:
                cur = cur.children[letter]
                if not cur.isEnd:
                    break           
            if cur.isEnd and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
            
        return res
            
        #my brute method before tring trie implemetation
        # if not words:
        #     return []
        # words.sort()
        # res = ['']
        # longest = ''
        # for word in words:
        #     if word[:-1] in res:
        #         if len(word) > len(longest):
        #             longest = word
        #         res.append(word)
        # return longest
        
        
                
                
