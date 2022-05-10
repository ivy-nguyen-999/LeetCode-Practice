class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        # to record which land already visited
        visit = set()
        
        def dfs(row, column, visit):
            #base cases
            if((row, column) in visit or row < 0 or row == ROWS 
               or column < 0 or column == COLUMNS or grid[row][column] == '0'):
                return
            visit.add((row, column))
            dfs(row - 1, column, visit)
            dfs(row + 1, column, visit)
            dfs(row, column - 1, visit)
            dfs(row, column + 1, visit)
        
        result = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (grid[row][column] == '1') and ((row, column) not in visit):
                    result += 1
                    dfs(row, column, visit)
        
        return result