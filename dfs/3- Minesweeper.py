class Solution(object):
    def addNumbersToAjacentMines(self, board):
        stack = []
        num_board = [["0"]*len(board[0]) for i in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="M":
                    stack.append([r,c])
        #Stack has all the mines -> updated each adjacent nodes to a number 
        while len(stack)>0:
            current_mine = stack.pop()
            num_board = self.updateNumBoard(current_mine, board, num_board)
        return num_board

    def updateNumBoard(self, position, board, num_board):
        m = position[0]
        n = position[1]
        for r in range(m-1, m+2):
            for c in range(n-1, n+2):
                if (r < len(board) and r>=0) and (c < len(board[0]) and c>=0):
                    if (r==m and c!=n) or (r!=m and c==n) or (r!=m and c!=n):
                        num_board[r][c] = str(int(num_board[r][c])+1)
        return num_board
    
    def positionsToExplore(self, position, board):
        m = position[0]
        n = position[1]
        all_positions = []
        for r in range(m-1, m+2):
            for c in range(n-1, n+2):
                if (r < len(board) and r>=0) and (c < len(board[0]) and c>=0):
                    if (r==m and c!=n) or (r!=m and c==n) or (r!=m and c!=n):
                        all_positions.append([r, c])
        return all_positions

    def updateConditions(self, position, board):
        num_board = self.addNumbersToAjacentMines(board)
        stack = []
        stack.append(position)
        while len(stack)>0:
            current_position = stack.pop()
            x = current_position[0]
            y = current_position[1]
            if board[x][y] == "M":
                board[x][y] = "X"
            elif board[x][y] == "E" and num_board[x][y] != "0":
                board[x][y] = num_board[x][y]
            elif board[x][y] == "E" and num_board[x][y] == "0":
                board[x][y] = "B"
                all_positions = self.positionsToExplore(current_position, board)
                for position in all_positions:
                    if position not in stack:
                        stack.append(position)
        return board
        
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        return self.updateConditions(click, board)

s = Solution()
#board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
#click = [3,0]
board = [["B", "1", "E", "1", "B"],["B", "1", "M", "1", "B"],["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
click = [1,2]
print(s.updateBoard(board, click))

#Uber