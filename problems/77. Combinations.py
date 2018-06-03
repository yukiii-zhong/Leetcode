class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(start, n, k, temp):
            if k == 0:
                self.res.append(temp)
                return
            elif start > n:
                return
            else:
                for i in range(start, n + 1):
                    if n - i < k - 1: break
                    dfs(i + 1, n, k - 1, temp + [i])

        dfs(1, n, k, [])
        return self.res