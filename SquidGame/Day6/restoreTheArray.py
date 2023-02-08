class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
         # Create a dictionary of the adjacent pairs
        d = {}
        for pair in adjacentPairs:
            if pair[0] not in d:
                d[pair[0]] = []
            if pair[1] not in d:
                d[pair[1]] = []
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0])
        # Find the start of the array
        start = None
        for key in d:
            if len(d[key]) == 1:
                start = key
                break
        # Create the array
        res = [start]
        while len(res) < len(adjacentPairs) + 1:
            res.append(d[res[-1]].pop())
            d[res[-1]].remove(res[-2])
        return res