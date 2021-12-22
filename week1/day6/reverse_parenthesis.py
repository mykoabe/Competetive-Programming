class Solution:
     def reverseParentheses(self, s: str) -> str:
        stack = []
        ln = len(s)
        for i in range(ln):
            if s[i] != ')':
                 stack.append(s[i])
                 print(s[i])
            else:
                reverse = []
                while stack and stack[-1] != '(':
                    reverse.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                    for k in reverse: 
                        stack.append(k)
        return ''.join(stack)
sol = Solution()
print(sol.reverseParentheses("(u(love)i)"))