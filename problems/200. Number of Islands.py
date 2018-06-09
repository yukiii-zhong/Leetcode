class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid[0]) == 0: return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not (i - 1 >= 0 and grid[i - 1][j] == '1') and not (
                        j - 1 >= 0 and grid[i][j - 1] == '1'):
                    count += 1
        return count

print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))