class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        if n == 0:
            return 0

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


print(Solution().climbStairs(35))

