import math

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3

        return n==1


    def isPowerOfThree2(self, n):
        if n < 1: return False
        x = math.log(n, 3)
        return abs(round(x) - x) < 0.000001


print(Solution().isPowerOfThree2(243))

print(math.log(243,3))

print(3**5)