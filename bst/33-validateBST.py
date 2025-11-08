# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev = float('-inf')
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val<=self.prev:
            return False
        self.prev = root.val
        return self.isValidBST(root.right)
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        left = right = True
        if root.left:
            left = self.isValidBST(root.left)
        if self.prev is not None:
            if root.val<=self.prev:
                return False
        self.prev = root.val
        if root.right:
            right = self.isValidBST(root.right)
        return left and right

# Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree/