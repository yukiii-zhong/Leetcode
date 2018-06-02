class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        res = [0, 1]

        for i in range(1, n):
            temp = []
            for j in range(len(res) - 1, -1, -1):
                temp.append(res[j] + 2 ** i)
            res += temp

        return res