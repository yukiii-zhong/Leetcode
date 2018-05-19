class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)

        if m == 0: return 0
        n = len(matrix[0])
        area = 0

        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:

                    if i - 1 >= 0 and j - 1 >= 0:
                        pre = matrix[i - 1][j - 1]
                        if pre > 0:
                            for x in range(1, pre + 1):
                                if matrix[i - x][j] > 0 and matrix[i][j - x] > 0:
                                    matrix[i][j] += 1
                                else:
                                    break
                    if matrix[i][j] > area:
                        area = matrix[i][j]
        return area ** 2