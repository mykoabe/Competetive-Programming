class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, curr = [], []
        currLen = 0
        for word in words:
            if currLen + len(word) + len(curr) > maxWidth:
                if len(curr) == 1:
                    res.append(curr[0] + " " * (maxWidth - currLen))
                else:
                    spaces = (maxWidth - currLen) // (len(curr) - 1)
                    extra = (maxWidth - currLen) % (len(curr) - 1)
                    for i in range(extra):
                        curr[i] += " "
                    res.append((" " * spaces).join(curr))
                curr = []
                currLen = 0
            curr.append(word)
            currLen += len(word)
        res.append(" ".join(curr) + " " * (maxWidth - currLen - len(curr) + 1))
        return res
