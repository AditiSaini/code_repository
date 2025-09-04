# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.val_dict = {}
        self.mode = 0
        self.nodes = []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root.left:
            self.findMode(root.left)
        if root.right:
            self.findMode(root.right)
        if root.val in self.val_dict:
            self.val_dict[root.val] += 1
        else:
            self.val_dict[root.val] = 1
        if self.val_dict[root.val]>self.mode:
            self.nodes = [root.val]
            self.mode = self.val_dict[root.val]
        elif self.val_dict[root.val]==self.mode:
            self.nodes.append(root.val)
        return self.nodes