class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        row, col = len(board), len(board[0])
        
        if row < 2 or col < 2:
            return board
      
        for r in range(row):
            self.dfs(board, r, 0, row, col)
            self.dfs(board, r, col-1, row, col)
            
        for c in range(col):
            self.dfs(board, 0, c, row, col)
            self.dfs(board, row-1, c, row, col)
            
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "meku":
                    board[r][c] = "O"
                    
                    
    def dfs(self, board, r, c, row, col):
        directions = [(-1,0), (1, 0), (0,-1), (0,1)]
        if 0 <= r < row and 0 <= c < col and board[r][c] == "O":
            board[r][c] = "meku"
            for d in directions:
                self.dfs(board, r+d[0], c+d[1], row, col)
                    
               
        
            
            
                    
                    
                    
                    
                    
                
                