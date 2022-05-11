class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        # to record which land already visited
        visit = set()
        def bfs(row, column):
            q = collections.deque()
            visit.add((row, column))
            q.append((row, column))
            
            while q:
                row, column = q.popleft()
                direction = [[0,1], [1,0], [0,-1], [-1,0]]
                
                for dr, dc in direction:
                    r, c = row + dr, column + dc
                    if (r in range(ROWS) and c in range(COLUMNS) and
                        grid[r][c] == '1' and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                
        result = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (grid[row][column] == '1') and ((row, column) not in visit):
                    result += 1
                    bfs(row, column)
        
        return result