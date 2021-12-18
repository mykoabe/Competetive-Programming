from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack += [int(val2 - val1)]
            elif i == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack += [int(val1 + val2)]
            elif i == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack += [int(val1 * val2)]
            elif i == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                if val1 != 0:
                    stack += [int(val2 / val1)]
            else:
                stack += [int(i)]
        return stack.pop()
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
                
                