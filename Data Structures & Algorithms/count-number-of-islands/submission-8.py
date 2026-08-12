class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            bfs(r+1, c)
            bfs(r-1, c)
            bfs(r, c+1)
            bfs(r, c-1)


        for row in range(ROWS): 
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        
        return islands