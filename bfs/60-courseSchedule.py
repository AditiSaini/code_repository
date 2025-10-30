from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree_count = defaultdict(int)
        for a,b in prerequisites:
            if b in graph:
                graph[b].append(a)
            else:
                graph[b]=[a]
            indegree_count[a]+=1
        queue = deque()
        visited = set()
        #Gets all the courses without conflicts
        for i in range(numCourses):
            if i not in indegree_count:
                queue.append(i)
        while queue:
            course = queue.popleft()
            visited.add(course)
            if course in graph:
                for neighbor in graph[course]:
                    if neighbor not in visited:
                        indegree_count[neighbor]-=1
                        if indegree_count[neighbor]==0:
                            queue.append(neighbor)
        if len(visited)==numCourses:
            return True
        return False 

# Leetcode Link: https://leetcode.com/problems/course-schedule