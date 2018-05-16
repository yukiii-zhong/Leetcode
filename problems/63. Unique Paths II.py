class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def helper(A):
            m = len(A)
            n = len(A[0])

            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    # Finish
                    if i == m-1 and j == n-1:
                        A[i][j] ^=1
                        continue

                    if A[i][j] == 1:
                        A[i][j] = 0
                    else:
                        if i == m-1:
                            A[i][j] = A[i][j+1]
                        elif j == n-1:
                            A[i][j] = A[i+1][j]
                        else:
                            A[i][j] = A[i+1][j] + A[i][j+1]

            return A[0][0]

        return helper(obstacleGrid)

print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))