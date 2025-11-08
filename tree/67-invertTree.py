# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        left = right = None
        if root.left:
            left = self.invertTree(root.left)
        if root.right:
            right = self.invertTree(root.right)
        temp = left
        root.left = right 
        root.right = temp 
        return root
    
# Leetcode link : https://leetcode.com/problems/invert-binary-tree/