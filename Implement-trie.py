class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True
        
    def search(self, word: str) -> bool:
        
        current = self.root
        for w in word:
            current = current.children.get(w)
            if not current:
                return False
        return current.isword
           
    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for p in prefix:
            curr = curr.children.get(p)
            if not curr:
                return False
        return True
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
