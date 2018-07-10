class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []

        self.table = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        self.midset = {'0', '1', '8'}
        self.ans = []

        def helper(i, n, temp):
            # Edge:
            if i == n + 1:
                self.ans.append(temp)
                return
                # Common Case
            mid = (n + 1) / 2
            if i == mid:
                for num in self.midset:
                    helper(i + 1, n, temp + num)
            elif i < mid:
                for num in self.table:
                    if i == 1 and num == '0':
                        continue
                    else:
                        helper(i + 1, n, temp + num)
            elif i > mid:
                helper(i + 1, n, temp + self.table[temp[n-i]])

        helper(1, n, '')
        return self.ans

print(Solution().findStrobogrammatic(2))