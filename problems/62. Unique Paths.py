class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def helper(m,n,seen):
            if (m,n) in seen: return seen[(m,n)]

            if (m == 2 and n == 1) or (n==2 and m==1) or (m==1 and n ==1):
                return 1

            count = 0
            if m-1 >= 1:
                count += helper(m-1,n,seen)
                seen[(m-1,n)] = count
            if n-1 >=1:
                temp = helper(m, n-1, seen)
                seen[(m,n-1)] = temp
                count += temp

            return count

        return helper(m,n,{})

    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # finish A[0,0]
        # start A[m-1,n-1]

        A = [[0] * n] * m

        A[0][0] = 1

        for i in range(1, m):
            A[i][0] = 1

        for j in range(1, n):
            A[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                A[i][j] = A[i - 1][j] + A[i][j - 1]

        return A[m - 1][n - 1]


print(Solution().uniquePaths2(21,10))