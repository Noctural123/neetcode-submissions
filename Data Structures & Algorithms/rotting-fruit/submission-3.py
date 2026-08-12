class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        minutes = 0

        def add_row(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return 
            q.append((r,c))
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 0
                add_row(r+1, c)
                add_row(r-1, c)
                add_row(r, c+1)
                add_row(r, c-1)
            if q:
                minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes 
