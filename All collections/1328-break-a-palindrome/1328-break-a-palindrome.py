class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        s = list(palindrome)
        for i in range(len(s)):
            if s[i] != 'a':
                s[i] = 'a'
                break
                
        if s != s[::-1]:
            return "".join(s)
        
        s = list(palindrome)
        for i in range(len(s)-1, -1, -1):
            if s[i] =="a":
                s[i] = "b"
                break
                
        return "".join(s)