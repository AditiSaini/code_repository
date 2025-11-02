# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0
    def goodNodesTraversal(self, root: TreeNode, maxNode: int) -> int:
        if root is None:
            return 0
        if root.left:
            self.goodNodesTraversal( root.left, max(root.val, maxNode))
        if root.val>= maxNode:
            self.count +=1
        if root.right:
            self.goodNodesTraversal( root.right, max(root.val, maxNode))
        return self.count

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesTraversal(root, root.val)
    
# Leetcode Link : https://leetcode.com/problems/count-good-nodes-in-binary-tree