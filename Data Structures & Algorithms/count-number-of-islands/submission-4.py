class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    temp_row = row + dr
                    temp_col = col + dc

                    if (temp_row in range(ROWS) and
                        temp_col in range(COLS) and
                        grid[temp_row][temp_col] == "1" and
                        (temp_row, temp_col) not in visited):
                        q.append((temp_row, temp_col))
                        visited.add((temp_row, temp_col))

        



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands