class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)


        for r in range(9):
            for c in range(9):
                currNum = board[r][c]
                if currNum== ".":
                    continue
                
                
                if currNum in cols[c] or currNum in rows[r] or currNum in box[(r//3, c//3)]:
                    return False
                

                rows[r].add(currNum)
                cols[c].add(currNum)
                box[(r//3, c//3)].add(currNum)
        

        return True
                    
                    
        