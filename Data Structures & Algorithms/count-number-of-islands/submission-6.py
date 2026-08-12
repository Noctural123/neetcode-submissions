class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    temp_row, temp_col = dr + row, dc + col

                    if (temp_row in range(ROWS) and
                        temp_col in range(COLS) and
                        grid[temp_row][temp_col] == "1" and
                        (temp_row, temp_col) not in visited):
                        q.append((temp_row, temp_col))
                        visited.add((temp_row,temp_col))
                


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row, col)
                    islands += 1
        
        return islands