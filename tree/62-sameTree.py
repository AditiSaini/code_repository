class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = right = False
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right) 
        return left and right 

# Leetcode Link : https://leetcode.com/problems/same-tree