class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Whem OG[m-1][n-1] ==0
        count = [[0] * n] * m

        count[m - 1][n - 1] = 1

        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 1:
                count[i][n - 1] = 0
            else:
                count[i][n - 1] = count[i + 1][n - 1]

        for j in range(n - 2, -1, -1):
            if obstacleGrid[m - 1][j] == 1:
                count[m - 1][j] = 0
            else:
                count[m - 1][j] = count[m - 1][j + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    count[i][j] = 0
                else:
                    count[i][j] = count[i + 1][j] + count[i][j + 1]

        return count[0][0]

print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))