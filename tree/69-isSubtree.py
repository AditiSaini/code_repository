from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        left = right = False
        if root1 and root2 and root1.val == root2.val:
            left = self.isSameTree(root1.left, root2.left)
            right = self.isSameTree(root1.right, root2.right)
        return left and right

    def isSubtreeIterative(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur.val == subRoot.val:
                if self.isSameTree(cur, subRoot):
                    return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return False
    def isSubtreeRecursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left = right = False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        return left or right