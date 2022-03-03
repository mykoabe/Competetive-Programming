# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return
        
        queue = deque([root])
        result = []
        
        while queue:
            cur_level_sum = 0
            lenn = len(queue)
            for i in range(lenn):
                node = queue.popleft()
                cur_level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #print(cur_level_sum)
            result.append(float(cur_level_sum) / lenn)
        
        return result
                