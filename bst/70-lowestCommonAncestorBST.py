# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        if parent node is either node1 or node2 => return parent node
        if node1 is on one side and node is on the other side: return parent node
        if both node on one side => traverse to the side where the results are
        """
        #If root is the same value as p or q
        if root.val == p.val or root.val == q.val:
            return root
        #If p and q are on two different sides of the BST => return root
        elif (p.val<root.val and root.val<q.val) or (q.val<root.val and root.val<p.val):
            return root
        #If both p and q are on the left side
        elif (p.val<root.val and q.val<root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        #If both p and q are on the right side
        elif (p.val>root.val and q.val>root.val):
            return self.lowestCommonAncestor(root.right, p, q)

# Leetcode link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree