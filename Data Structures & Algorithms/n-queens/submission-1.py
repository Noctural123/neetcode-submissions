class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]

        col = set()
        diag = set()
        anti_diag = set()
        res = []


        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (c in col) or (r+c in anti_diag) or (r-c in diag):
                    continue
                
                col.add(c)
                diag.add(r-c)
                anti_diag.add(r+c)
                board[r][c] = 'Q'

                backtrack(r+1)

                col.remove(c)
                diag.remove(r-c)
                anti_diag.remove(r+c)
                board[r][c] = '.'

        backtrack(0)
        return res