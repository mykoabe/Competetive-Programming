class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        #using monotonic stack and greedy algorithem
        
        stack = []
        
        for i, letter in enumerate(s):
            
            if not stack:
                stack.append(letter)
            elif letter in stack:
                continue
            else:
                while stack and (letter < stack[-1]):
                    if stack[-1] in s[i + 1:]:
                        stack.pop()
                    else:
                        break
                        
                stack.append(letter)
                
        return "".join(stack)