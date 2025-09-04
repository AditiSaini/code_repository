# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findSum(root, currentSum):
            if root is None:
                return False
            if root.left is None and root.right is None:
                return currentSum+root.val==targetSum
            left_sum = right_sum = False
            if root.left:
                left_sum = findSum(root.left, currentSum+root.val)
            if root.right:
                right_sum = findSum(root.right, currentSum+root.val)
            return left_sum or right_sum
        return findSum(root, 0)

# Leetcode Link: https://leetcode.com/problems/path-sum