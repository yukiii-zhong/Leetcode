class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]*(rowIndex+1)

        if rowIndex <=1: return ans

        pre = self.getRow(rowIndex-1)

        for i in  range(1,rowIndex):
            ans[i] = pre[i-1] + pre[i]

        return ans

print(Solution().getRow(4))