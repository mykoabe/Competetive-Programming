class Solution:
    def calculate(self, s: str) -> int:
        
        stack=[]
        operators="+-*/"
        nums="0123456789"
        
        currentNum = ""
        currentOperator="+"
        

        def division(num1,num2):
            if num1>=0 or num1%num2==0:
                return num1//num2
            else:
                return num1//num2+1

        for i in range(len(s)):
            char=s[i]
            if char==" " and i != len(s)-1:
                continue
            if char in nums:
                currentNum+=char 
            if char in operators or i==len(s)-1:
                if currentOperator == "+":
                    stack.append(int(currentNum))
                elif currentOperator == "-":
                    stack.append(-int(currentNum))
                elif currentOperator == "*":
                    stack[-1] *= int(currentNum)
                else:
                    stack[-1] = division(stack[-1],int(currentNum))
                currentNum=""
                currentOperator=char

        return sum(stack)
