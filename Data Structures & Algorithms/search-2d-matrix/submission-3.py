class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // COLS, mid % COLS

            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        
        return False


        # 0 1  2  3 
        # 4 5  6  7
        # 8 9 10 11


        # row = 4 // 4 -> index // COLS
        # col = 4 % 4 -> index % COLS