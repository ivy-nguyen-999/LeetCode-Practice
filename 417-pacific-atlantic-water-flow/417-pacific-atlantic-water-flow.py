class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #get the row and column
        ROWS, COLUMNS = len(heights), len(heights[0])
        #sets to record visited nodes
        pacific, atlantic = set(), set()
        
        def dfs(row, column, visit, prevHeight):
            #base cases:
            if((row, column) in visit or row < 0 or row == ROWS 
               or column < 0 or column == COLUMNS or heights[row][column] < prevHeight):
                return
            #recursive
            visit.add((row, column))
            dfs(row + 1, column, visit, heights[row][column])
            dfs(row - 1, column, visit, heights[row][column])
            dfs(row, column + 1, visit, heights[row][column])
            dfs(row, column - 1, visit, heights[row][column])
        
        for column in range(COLUMNS):
            dfs(0, column, pacific, heights[0][column])
            dfs(ROWS - 1, column, atlantic, heights[ROWS - 1][column])
        
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLUMNS - 1, atlantic, heights[row][COLUMNS - 1])
        
        res = []
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (row, column) in pacific and (row, column) in atlantic:
                    res.append((row, column))
        
        return res
                
        
        