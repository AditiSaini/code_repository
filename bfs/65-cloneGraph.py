"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            for neigh in cur.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    queue.append(neigh)
                visited[cur].neighbors.append(visited[neigh])
        return visited[node]
    
# Leetcode Link : https://leetcode.com/problems/clone-graph/