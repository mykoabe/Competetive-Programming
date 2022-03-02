"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        def helper(node):
            if(node==None):
                return 0
            else:
                m=0
                for i in node.children:
                    m=max(m,helper(i))
                return 1+m
        
        return helper(root) 
            