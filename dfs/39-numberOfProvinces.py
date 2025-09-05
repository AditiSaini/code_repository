class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = [False] * size
        stack = []
        provinces = 0
        for i in range(size):
            if not visited[i]:
                stack.append(i)
                while len(stack)>0:
                    node = stack.pop()
                    visited[node]=True
                    for neighbor in range(size):
                        if isConnected[node][neighbor]==1 and not visited[neighbor]:
                            stack.append(neighbor)
                provinces+=1
        return provinces
    
# Leetcode Link: https://leetcode.com/problems/number-of-provinces/