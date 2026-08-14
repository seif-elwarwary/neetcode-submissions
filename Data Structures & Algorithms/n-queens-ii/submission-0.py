class Solution:
    def totalNQueens(self, n: int) -> int:
        def isSafe(r: int, c: int, board):
            row = r - 1
            while row >= 0: # check column
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0: # check left diagonal
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):# check right diagonal
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True
        res=[]
        board = [['.']*n for _ in range(n)]
        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if isSafe(r,c,board):
                    board[r][c]='Q'
                    dfs(r+1)
                    board[r][c]='.'

        dfs(0)
        return len(res)