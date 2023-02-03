# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0, 0)]
        res = defaultdict(list)
        while queue:
            for node, col, row in queue:
                res[(col, row)].append(node.val)
            new_queue = []
            for node, col, row in queue:
                if node.left:
                    new_queue.append((node.left, col - 1, row + 1))
                if node.right:
                    new_queue.append((node.right, col + 1, row + 1))
            queue = new_queue
        d = defaultdict(list)
        for col, row in res:
            val = sorted(res[(col, row)])
            d[col].extend(val)
        return [d[c] for c in sorted(d.keys())]
        
        
        