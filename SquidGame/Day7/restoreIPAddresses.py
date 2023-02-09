class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def helper(s, path, res):
            if len(path) == 4 and not s:
                res.append(".".join(path))
                return
            # Base case
            if len(path) == 4 or not s:
                return
            for i in range(1, 4):
                if i <= len(s) and (s[0] != "0" or i == 1) and int(s[:i]) <= 255:
                    path.append(s[:i])
                    # Recurse
                    helper(s[i:], path, res)
                    path.pop()
        helper(s, [], res)
        return res