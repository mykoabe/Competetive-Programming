class Solution:
    def __init__(self):
        self.items = []
    def push(self, file):
        self.items.append(file)
    def peek(self):
        return self.items.pop()
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items) == 0
def matchingParenthesis(strings):
    stack = Solution()
    parenthesisDictionary = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    openers = parenthesisDictionary.keys()
    index = 0
    while index < len(strings):
        symbol = strings[index]
        if symbol in openers:
            stack.push(symbol)
        else: 
            if stack.isEmpty():
                return False
            else: 
                lastItem = stack.pop() 
                if symbol != parenthesisDictionary[lastItem]:
                    return False
        index+=1
    if stack.isEmpty():
        return True
    return False
    print(symbol)
print(matchingParenthesis("(})"))

def palindromeChecker(string):
    st = string[:]
    
palindromeChecker("hello")


    

