# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count = 1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left = right = None
        if root.left:
            left = self.kthSmallest(root.left, k)
            if left is not None:
                return left
        if self.count==k:
            return root.val
        self.count+=1
        if root.right:
            right = self.kthSmallest(root.right, k)
            if right is not None:
                return right

# Leetcode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/