class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]

        ib, ie, jb, je = 0, n - 1, 0, n - 1

        x = 1
        while True:
            for j in range(jb, je + 1):
                res[ib][j] = x
                x += 1
            ib += 1
            if ib > ie: break

            for i in range(ib, ie + 1):
                res[i][je] = x
                x += 1
            je -= 1
            if jb > je: break

            for j in range(je, jb - 1, -1):
                res[ie][j] = x
                x += 1
            ie -= 1
            if ib > ie: break

            for i in range(ie, ib - 1, -1):
                res[i][jb] = x
                x += 1
            jb += 1
            if jb > je: break

        return res



