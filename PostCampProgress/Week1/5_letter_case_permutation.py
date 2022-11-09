# using recursion -> backtacking
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def dfs(i, path):
            if i == len(S):
                res.append(path)
                return
            if S[i].isalpha():
                dfs(i+1, path + S[i].lower())
                dfs(i+1, path + S[i].upper())
            else:
                dfs(i+1, path + S[i])
        dfs(0, '')
        return res

    

