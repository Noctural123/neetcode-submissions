class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if top > bot:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        row = (top + bot) // 2
        while l <= r:
            col = (l + r) // 2

            if target > matrix[row][col]:
                l += 1
            elif target < matrix[row][col]:
                r -= 1
            else:
                return True
        
        return False
    

    # 0 1 2 3
    # 4 5 6 7
    # 8 9 10 11

    # 1   2   4   8 
    # 10  11  12  13
    # 14  20  30  40

    # 3 x 4

    # l = 0
    # r = 11

    # mid = 5
    # mid_row = 