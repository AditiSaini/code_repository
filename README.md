### Concepts Learnt
- BFS is implemented with queues
- DFS is implemented with stacks
- BFS/ DFS algorithms can be used with indegree and outdegree to count dependence
- BFS/ DFS graph source<->sink can be reversed based on the need look at q26 course scheduling 
- Sorting using Python Lambda function: intervals_sorted = sorted(intervals, key=lambda x: x[0]). This sorts elements from list intervals based on the first element in the list. E.g. [[2,4], [1,5],[4,6]] => [[1,5],[2,4],[4,6]]
- In order traversal can be used to validate Binary Search Tree (q33)
- In order traversal of a BST gives a sorted list of values
- Add memoization to a recursive question by adding "from functools import lru_cache" and @lru_cache(None) over the function, e.g. in q37