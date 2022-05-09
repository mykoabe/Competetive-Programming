class Solution:
    def simplifyPath(self, path: str) -> str:
        #let s_str is equal to separated string
        s_str = path.split('/')
        result = []
        n = len(s_str)
        for i in range(n):
            if s_str[i] and s_str[i] != '.' and s_str[i] != '..':
                result.append(s_str[i])
            if s_str[i] == '..':
                if result:
                    result.pop() 
        return '/' + '/'.join(result)
        
