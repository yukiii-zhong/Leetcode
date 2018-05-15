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

print(Solution().uniquePaths(21,10))