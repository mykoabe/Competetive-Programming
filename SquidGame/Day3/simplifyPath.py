class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)
        #
        



        #let s_str is equal to separated string
        # s_str = path.split('/')
        # print(s_str)
        # result = []
        # n = len(s_str)
        # for i in range(n):
        #     if s_str[i] and s_str[i] != '.' and s_str[i] != '..':
        #         result.append(s_str[i])
        #     if s_str[i] == '..':
        #         if result:
        #             result.pop() 
        # #print(s_str)
        # return '/' + '/'.join(result)
        