class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
        
class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            curr_node = curr_node.children[c]
        curr_node.isEnd = True
        
            
    def search(self, word: str) -> bool:
        def helper(word, index, root):
            if root == None: return False
            if index == len(word):
                return root.isEnd
            if word[index] != '.':
                return root != None and helper(word, index+1,                 root.children.get(word[index]))
            else:
                for child in root.children.values():
                    if helper(word, index + 1, child):
                        return True
        return helper(word, 0, self.root)
            
            
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
