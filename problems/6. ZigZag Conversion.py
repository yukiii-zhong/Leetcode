class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s

        turned = [""] * numRows

        r = 0

        for i in range(len(s)):
            turned[r] += s[i]
            if i % ((numRows - 1) * 2) < (numRows - 1):
                r += 1
            else:
                r -= 1

        return "".join(turned)

