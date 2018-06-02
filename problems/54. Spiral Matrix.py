class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])

        rb, re, cb, ce = 0, m - 1, 0, n - 1
        res = []

        while True:
            for j in range(cb, ce + 1):
                res.append(matrix[rb][j])
            rb += 1
            if rb > re: break

            for i in range(rb, re + 1):
                res.append(matrix[i][ce])
            ce -= 1
            if cb > ce: break

            for j in range(ce, cb - 1, -1):
                res.append(matrix[re][j])
            re -= 1
            if rb > re: break

            for i in range(re, rb - 1, -1):
                res.append(matrix[i][cb])
            cb += 1
            if cb > ce: break
        return res