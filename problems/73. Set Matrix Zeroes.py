class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        Frow = True
        Fclm = True

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                Fclm = False
                break

        for j in range(n):
            if matrix[0][j] == 0:
                Frow = False
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if Frow == 0:
            for j in range(n):
                matrix[0][j] = 0
        if Fclm == 0:
            for i in range(m):
                matrix[i][0] = 0
