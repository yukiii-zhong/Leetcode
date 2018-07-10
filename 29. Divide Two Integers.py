class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """
        - 边界问题
        - +/-
        """
        sign = 1
        if (dividend<0) ^ (divisor<0):
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)

        def help(dividend,divisor):
            if divisor>dividend: return 0
            cal = 1
            sum = divisor
            while sum+sum<=dividend:
                sum <<=1
                cal <<=1
            return cal + help(dividend-sum,divisor)

        res = help(dividend,divisor)

        if sign<1: res = -res

        return min(max(-(1<<31),res),1<<31-1)