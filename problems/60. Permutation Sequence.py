class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = ''

        def dfs(nums, k):
            n = len(nums)
            if n == 0: return
            # (n-1)!
            if k == 0:
                self.res += str(nums[-1])
                del (nums[-1])
                dfs(nums, 0)
                return
            temp = 1
            for i in range(1, n):
                temp *= i
            (a, b) = divmod(k, temp)
            a += 1 if b > 0 else 0
            self.res += str(nums[a - 1])
            del (nums[a - 1])
            dfs(nums, b)

        nums = [i for i in range(1, n + 1)]
        dfs(nums, k)
        return self.res