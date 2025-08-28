"""
Approach 1: Graph + BFS
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        #Convert values in nums into graph  
        graph = dict()
        size = len(nums)-1
        for idx in range(len(nums)):
            cur_num = nums[idx]
            for idx2 in range(cur_num, 0, -1):
                edge = min(idx+idx2, size)
                if idx not in graph:
                    graph[idx] = [edge]
                elif edge not in graph[idx] and idx!=edge:
                    graph[idx].append(edge)

        #Perform BFS for finding min path 
        start_index = 0
        min_path = size
        #Queue has min_distance, path
        queue = [(0, [start_index])]
        visited = set([start_index])
        while len(queue)>0:
            cur_min_distance, cur_path = queue.pop(0)
            last_node_path = cur_path[-1]
            if last_node_path not in graph:
                continue
            for value in graph[last_node_path]:
                if value not in visited:
                    to_add = [cur_min_distance+1, cur_path + [value]]
                    queue.append(to_add)
                    visited.add(value)
                    if value == size:
                        min_path = min(min_path, cur_min_distance+1)
        return min_path
    
"""
Approach 2: How far can we reach with current jumps
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0 
        current_boundary = 0 
        jumps = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= (len(nums)-1):
                return jumps+1
            elif i == current_boundary:
                current_boundary = max_reach 
                jumps+=1
        return jumps 
    
# Leetcode Link: https://leetcode.com/problems/jump-game-ii/