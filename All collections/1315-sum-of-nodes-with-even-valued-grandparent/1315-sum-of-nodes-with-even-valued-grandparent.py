# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        evn_child_sum = 0
        def helper(node):
            
            nonlocal evn_child_sum
            if not node:
                return
            
            if node.val%2==0:
                
                if node.right and node.right.right:
                    evn_child_sum+=node.right.right.val
                if node.right and node.right.left:
                    evn_child_sum+=node.right.left.val
                if node.left and node.left.left:
                    evn_child_sum += node.left.left.val
                if node.left and node.left.right:
                    evn_child_sum += node.left.right.val
                    
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return evn_child_sum
                
        
        
        
                
                