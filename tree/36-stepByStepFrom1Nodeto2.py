#My Solution 1 (Gives Memory Limit Exceeded Error but works)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getDirectionsForNode(root, curPath, targetVal):
            if root is None:
                return None
            if root.val == targetVal:
                return curPath
            if root.left:
                left = getDirectionsForNode(root.left, curPath+['L'], targetVal)
                if left:
                    return left
            if root.right:
                right = getDirectionsForNode(root.right, curPath+['R'], targetVal)
                if right:
                    return right
            return None
        node_start_dir = getDirectionsForNode(root, [], startValue)
        node_dest_dir = getDirectionsForNode(root, [], destValue)
        i = 0
        while i < len(node_start_dir) and i < len(node_dest_dir) and node_start_dir[i] == node_dest_dir[i]:
            i += 1
        return "U" * (len(node_start_dir) - i) + ''.join(node_dest_dir[i:])

#GPT Improved Solution 2
"""
Instead of copying curPath every time, maintain one list, append as you go down, and pop when backtracking. That way, you reuse the same list without creating new ones at each depth.
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            # try left
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            # try right
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False
        # find paths using a shared path list
        pathStart, pathDest = [], []
        findPath(root, startValue, pathStart)
        findPath(root, destValue, pathDest)
        # find common prefix
        i = 0
        while i < len(pathStart) and i < len(pathDest) and pathStart[i] == pathDest[i]:
            i += 1
        # "U" for going up from start, then directions to dest
        return "U" * (len(pathStart) - i) + "".join(pathDest[i:])
