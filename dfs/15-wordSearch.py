from typing import List

class Solution:
    def existv1(self, board: List[List[str]], word: str) -> bool:
        # m -> number of rows, n -> number of columns
        m, n = len(board), len(board[0])

        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Helper function for DFS
        def dfs(i, j, idx):
            # If we've matched all characters in the word, return True
            if idx == len(word):
                return True
            
            # Save the current cell's character and mark the cell as visited
            temp, board[i][j] = board[i][j], '#'
            
            # Explore the 4 possible directions
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # Check if the next position is within bounds and matches the next character
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[idx]:
                    if dfs(ni, nj, idx + 1):  # Continue DFS for the next character
                        return True
            
            # Backtrack: Restore the original character and unmark the cell
            board[i][j] = temp
            return False
        
        # Try starting the DFS from each cell in the grid
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:  # If the first character matches
                    if dfs(i, j, 1):  # Start DFS from the next character (idx = 1)
                        return True
        
        # If no solution is found, return False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        #Check if the word size is lesser than the boxes in the board
        visited_size = len(board)*len(board[0])
        if len(word)>visited_size:
            return False
        #Have a matrix that keeps track of visited nodes
        visited = [[0]*len(board[0]) for _ in range(len(board))]
        #Store the first char of the word
        first_char = word[0]
        #Stack to keep track of positions to explore
        stack = []
        #Iterate through the board and look for char that match the first letter on the board
        # m-> number of rows, n-> number of cols
        for m in range(len(board)):
            for n in range(len(board[0])):
                #If this cell has not been visited
                if first_char==board[m][n]:
                    stack.append((m, n))
                    visited = [[0]*len(board[0]) for _ in range(len(board))]
                    isWordPresent = self.isWordPresent(stack, visited, board, word)
                    if isWordPresent:
                        return True
        return False 
                    
    def isWordPresent(self, stack, visited, board, word):
        if len(word)<2:
            return True
        #Performs DFS to find the word
        target_idx = 0
        toVisit = [[1,0], [-1,0], [0,1], [0,-1]]
        found_next_char = True
        done = False
        while len(stack)>0 and target_idx<len(word) and done ==False:
            m, n = stack.pop()
            if found_next_char:
                target_idx += 1
            found_next_char = False
            target_char = word[target_idx]
            for idx in toVisit:
                x= idx[0]
                y= idx[1]
                if (m+x)>=0 and (m+x)<len(board) and (n+y)>=0 and (n+y)<len(board[0]):
                    value_board = board[m+x][n+y]
                    if value_board == target_char and visited[m+x][n+y]==0:
                        found_next_char = True
                        stack.append((m+x, n+y))
            if found_next_char:
                visited[m][n] = 1
            if target_idx==len(word)-1 and found_next_char:
                done = True
        if found_next_char == False:
            return False
        return True 

s = Solution()
#Test Case 1
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
#Test Case 2
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
#Test Case 3
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
#Test Case 4
# board = [["a"]]
# word = "a"
#Test Case 5
# board = [["a","b"],["c","d"]]
# word = "acdb"
# Test Case 6
# board = [["C","A","A"],["A","A","A"],["B","C","D"]]
# word = "AAB"
# Test Case 7
# board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# word = "ABCESEEEFS"
# Test Case 8
# board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# word = "ABCEFSADEESE"
# Test Case 9
board = [["a","a","b","a","a","b"],["a","a","b","b","b","a"],["a","a","a","a","b","a"],["b","a","b","b","a","b"],["a","b","b","a","b","a"],["b","a","a","a","a","b"]]
word = "bbbaabbbbbab"
print(s.exist(board, word))