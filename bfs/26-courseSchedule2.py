class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        dependencies = [0]*numCourses
        for a,b in prerequisites:
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
            dependencies[a]+=1
        queue = []
        for i in range(len(dependencies)):
            if dependencies[i]==0:
                queue.append(i)
        order = []
        while len(queue)>0:
            node = queue.pop(0)
            order.append(node)
            if node in graph:
                for neighbor in graph[node]:
                    dependencies[neighbor]-=1
                    if dependencies[neighbor]==0:
                        queue.append(neighbor)
        return order if len(order)==numCourses else []
    
# Leetcode Link: https://leetcode.com/problems/course-schedule-ii/