class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return 0

        if x == 0:
            return x
        elif x < 0:
            return self.reverse(-x) * (-1)

        # x>0
        rev = 0
        while x > 0:
            x, rev = x // 10, x % 10 + rev * 10
            if rev > 2 ** 31 - 1:
                rev = 0
                break

        return rev

