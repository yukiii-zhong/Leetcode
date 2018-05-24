class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1: return s

        res = [""] * numRows

        r = 0
        step = -1

        for ch in s:
            res[r] += ch
            if r == numRows - 1 or r == 0:
                step *= -1
            r += step

        return "".join(res)