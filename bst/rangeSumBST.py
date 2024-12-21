from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recurseSumBST(node, total_sum):
            if node is None:
                return total_sum
            if node.val>= low and node.val<=high:
                total_sum+=node.val
            if node.right is not None and node.val<high:
                total_sum = recurseSumBST(node.right, total_sum)
            if node.left is not None and node.val>low:
                total_sum =recurseSumBST(node.left, total_sum)
            return total_sum
        return recurseSumBST(root, 0)
    def rangeSumBSTv2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recurseSumBSTv2(node):
            current_sum = 0
            left_sum = 0
            right_sum = 0
            if node is None:
                return total_sum
            if node.val>= low and node.val<=high:
                current_sum = node.val
            if node.val>low:
                left_sum = recurseSumBSTv2(node.left)
            if node.val<high:
                right_sum = recurseSumBSTv2(node.right)
            return total_sum + left_sum + right_sum
        return recurseSumBSTv2(root)

#Template code to build the tree
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

values = [10, 5, 15, 3, 7, None, 18]
root = build_tree(values)
low, high = 7, 15
solution = Solution()
result = solution.rangeSumBSTv2(root, low, high)
print(result)

#Meta