class Solution:
    def traverseDfs(self, visited, stack, grid):
        while len(stack)>0:
            m, n = stack.pop()
            visited[m][n] = 1
            all_directions = [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]            
            for (r, c) in all_directions:
                if r<len(grid) and r>=0 and c<len(grid[0]) and c>=0:
                    if grid[r][c] == "1" and visited[r][c]==0:
                        visited[r][c] = 1
                        stack.append((r, c))
        return visited
    
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for x in range(col)] for y in range(row)]
        stack = []
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    stack.append((row, col))
                    visited = self.traverseDfs(visited, stack, grid)
                    island_count+=1
        return island_count

        
