class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            if (i,j) in visited: return 0
            if i>=rows or i<0 or j>=cols or j<0 or grid[i][j]==0 : return 1
            visited.add((i,j))
            perim = dfs(i+1,j)
            perim += dfs(i-1,j)
            perim += dfs(i,j+1)
            perim += dfs(i,j-1)
            return perim
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i,j)
        return 0