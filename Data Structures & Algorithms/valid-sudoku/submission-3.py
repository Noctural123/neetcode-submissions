class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currNum = board[r][c]

                if currNum == ".":
                    continue

                if(currNum in col[c] or currNum in row[r] or currNum in box[r//3, c//3]):
                    return False
                

                row[r].add(currNum)
                col[c].add(currNum)
                box[r//3, c//3].add(currNum)

        
        return True

                    
                    
        