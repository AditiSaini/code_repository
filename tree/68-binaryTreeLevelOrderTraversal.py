# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def __init__(self):
        self.level_nodes = defaultdict(list)
        self.all_levels = []

    def findLevelNodes(self, root, level):
        if root is None:
            return 
        self.level_nodes[level].append(root.val)
        if root.left:
            self.findLevelNodes(root.left, level+1)
        if root.right:
            self.findLevelNodes(root.right, level+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.findLevelNodes(root, 0)
        for level in self.level_nodes:
            values = []
            for node in self.level_nodes[level]:
                values.append(node)
            self.all_levels.append(values)
        return self.all_levels
    
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        all_levels = []
        q = deque()
        q.append(root)
        while q:
            all_levels.append([node.val for node in q])
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return all_levels
    
# Leetcode link : https://leetcode.com/problems/binary-tree-level-order-traversal/