class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #Convert to graph
        graph = {}
        for a,b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a]=[b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b]=[a]

        #Get the height of the tree with each node as root node
        all_heights = {}
        final_nodes = []
        min_height = float('inf')
        for i in range(n):
            height = float('inf')
            visited = set()
            visited.add(i)
            stack = []
            stack.append((i, 0))
            max_height = 0 
            while stack:
                cur, height = stack.pop()
                max_height = max(max_height, height)
                if cur in graph:
                    for child in graph[cur]:
                        if child not in visited:
                            visited.add(child)
                            stack.append((child, height+1))
                        if len(visited)==n:
                            break
            all_heights[i] = max_height
            min_height = min(min_height, max_height)

        for node in all_heights:
            if all_heights[node] == min_height:
                final_nodes.append(node)
        
        return final_nodes
    
# WARNING: This is the brute force solution, can implement a better solution using leaf pruning method    
# Leetcode Link: https://leetcode.com/problems/minimum-height-trees