# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        #using dfs
        rows = []  
        def dfs(root, rows, row):
            if not root:
                return 
            if row == len(rows):
                rows.append([])
            rows[row].append(root.val)
            
            dfs(root.left, rows, row + 1)
            dfs(root.right, rows, row + 1)
                
        dfs(root, rows, 0)
        print(rows)
        return [max(r) for r in rows]
                
            
