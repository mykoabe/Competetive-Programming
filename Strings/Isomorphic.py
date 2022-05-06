class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        array1 = [-1]*256
        array2 = [-1]*256
        for i in range(len(s)):
            if array1[ord(s[i])] != array2[ord(t[i])]:
                return False
            array1[ord(s[i])]=i
            array2[ord(t[i])]=i
        return True
