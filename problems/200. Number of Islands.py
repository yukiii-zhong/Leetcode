class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def toWater(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = 0
                toWater(grid, i - 1, j)
                toWater(grid, i + 1, j)
                toWater(grid, i, j - 1)
                toWater(grid, i, j + 1)

        if not grid or len(grid[0]) == 0: return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    toWater(grid, i, j)
        return count
