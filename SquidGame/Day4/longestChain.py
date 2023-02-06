class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = {}
        for word in words:
            d[word] = 1
            for i in range(len(word)):
                successor = word[:i] + word[i+1:]
                if successor in d:
                    d[ word ] = max (d[word], 1 + d[successor])
        res = max(d.values())
        return res