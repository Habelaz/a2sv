class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def inbound(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        visited = set()
        def dfs(r,c):
            if  not inbound(r,c) or board[r][c] != 'O':
                return 
            board[r][c] = '#'

            for rc,cc in directions:
                nr = r + rc
                nc = c + cc
                dfs(nr,nc)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r in [0,len(board)-1] or c in [0,len(board[0])-1] ):
                    dfs(r,c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        
        return board