# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, depth):
            
            if node is None:
                return None, depth-1
            
            l_lca, l_depth = dfs(node.left, depth + 1)
            r_lca, r_depth = dfs(node.right, depth + 1)
            
            if l_depth == r_depth:
                return node, r_depth
            
            return (r_lca, r_depth) if r_depth > l_depth else (l_lca, l_depth)
        
        return dfs(root,0)[0]
            
            
        
        