class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        minutes = 0

        def addRows(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return
            
            visited.add((r,c))
            q.append((r,c))

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                addRows(r+1,c)
                addRows(r-1,c)
                addRows(r,c+1)
                addRows(r,c-1)
            
            if q:
                minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes

            