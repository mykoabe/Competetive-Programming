class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                leftSkip, rightSkip = s[left+1:right+1], s[left:right]
                return (leftSkip == leftSkip[::-1] or rightSkip == rightSkip[::-1])
            left, right = left + 1, right - 1
        return True
        