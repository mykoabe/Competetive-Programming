class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while(stack and stack[-1] == popped[0]):
                stack.pop()
                popped.pop(0)
        if(stack):
            return False
        return True