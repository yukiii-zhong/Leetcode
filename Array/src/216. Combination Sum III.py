class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        self.ans = []

        def dfs(k , n, start, list):

            if k == 0:
                if n == 0:
                    self.ans.append(list)
                return

            for i in range(start,10):

                if n-i<0: break

                dfs(k-1,n-i,i+1,list+[i])

        dfs(k,n,1,[])

        return self.ans