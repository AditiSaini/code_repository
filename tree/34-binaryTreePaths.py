# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def allPaths(root, path):
            if (root.left is None) and (root.right is None):
                paths.append(path)
            if root.left:
                allPaths(root.left, path+f"->{root.left.val}")
            if root.right:
                allPaths(root.right, path+f"->{root.right.val}")
        allPaths(root, f"{root.val}")
        return paths

# Leetcode Link: https://leetcode.com/problems/binary-tree-paths/