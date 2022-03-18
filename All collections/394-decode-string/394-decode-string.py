class Solution:
    def decodeString(self, s: str) -> str:
        length = len(s)

        prefixLastIndex = self.getPefixIndex(s)
        suffixStartIndex = self.getSuffixIndex(s, length)
        
        prefix = s[:prefixLastIndex]
        suffix = s[suffixStartIndex:]
        
        # code to decode
        code = s[prefixLastIndex:suffixStartIndex]
        
        if self.checkForFurtherDecode(code):
            return code
            
        num, bracketStartIndex = self.getNumeric(code)
        
        bracketEndIndex = self.getCloseBracketIndex(code, bracketStartIndex)

        curCode = code[bracketStartIndex+1:bracketEndIndex]
        remCode = code[bracketEndIndex+1:len(s)]

        ans = (int(num) * self.decodeString(curCode)) + self.decodeString(remCode)        
        
        return prefix+ans+suffix
    
    def getNumeric(self, code: str):
        num = ''
        for i,c in enumerate(code):
            if c.isdigit(): num += c
            else: break
        return (num,i)
    
    def checkForFurtherDecode(self, code:str):
        return '[' not in code and ']' not in code
            
    def getPefixIndex(self, s:str):
            for i,s in enumerate(s):
                if s.isdigit():
                    return i
        
    def getSuffixIndex(self, s:str, length):
            for i in range(length-1,-1,-1):
                if s[i] == ']':
                    return i+1
    
    def getCloseBracketIndex(self, code:str, startIndex:int):
        stack = ['[']
        curIndex = startIndex + 1
        length = len(code)
        if curIndex >= length: return length-1
        while stack and curIndex < length:
            if code[curIndex] == ']':
                stack.pop()
            if code[curIndex] == '[':
                stack.append('[')
            curIndex+=1
        return curIndex - 1