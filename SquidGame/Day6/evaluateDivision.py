class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        for i in range(len(equations)):
            if equations[i][0] not in d:
                d[equations[i][0]] = {}
            if equations[i][1] not in d:
                d[equations[i][1]] = {}
            d[equations[i][0]][equations[i][1]] = values[i]
            d[equations[i][1]][equations[i][0]] = 1 / values[i]
        # Create the results
        res = []
        for query in queries:
            if query[0] not in d or query[1] not in d:
                res.append(-1)
            elif query[0] == query[1]:
                res.append(1)
            else:
                res.append(self.dfs(query[0], query[1], d, set()))
        return res
    def dfs(self, start, end, d, visited):
        if start == end:
            return 1
        visited.add(start)
        for key in d[start]:
            if key not in visited:
                res = self.dfs(key, end, d, visited)
                if res != -1:
                    return res * d[start][key]
        return -1
