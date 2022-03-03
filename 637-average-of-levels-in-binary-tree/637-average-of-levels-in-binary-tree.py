# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q  = deque([root])
        average = []
        while q:
            step_sum = 0
            size = len(q)
            for i in range(size):
                current = q.popleft()
                step_sum += current.val
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            average.append((step_sum / size) + (10 ** (-5)))
        return average
                