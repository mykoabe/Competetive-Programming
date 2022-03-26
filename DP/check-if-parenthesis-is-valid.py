class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #dp
        opened, closed = 0, 0
        if len(s) % 2:
            return False
        
        nMin, nPos = 0, 0
        for i, j in zip(locked, s):
            if i == "1":
                if j == "(":
                    opened += 1
                else:
                    opened -= 1
            else:
                closed += 1
            if opened + closed < 0:
                return False
            nMin = max(0, opened - closed)
            nPos = max(nPos, math.ceil((nMin - opened + closed)/2))
        return opened - closed + 2*nPos <= 0
        
