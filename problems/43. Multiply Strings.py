class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0

        m = len(num1) - 1
        n = len(num2) - 1

        for j in range(m, -1, -1):
            for i in range(n, -1, -1):
                res += int(num1[i]) * int(num2[j]) * (10 ** (m - i)) * (10 ** (n - j))

        return res


print(Solution().multiply('90','10'))