class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                bfs(r + dr, c + dc)


        for row in range(ROWS): 
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        
        return islands