# another solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            return s == s[::-1]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
            left, right = left + 1, right - 1
        return True
    
    
        # left, right = 0, len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         leftSkip, rightSkip = s[left+1:right+1], s[left:right]
        #         return (leftSkip == leftSkip[::-1] or rightSkip == rightSkip[::-1])
        #     left, right = left + 1, right - 1
        # return True
# another solution