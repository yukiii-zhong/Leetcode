class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.helper(n,[])

    def helper(self, n, existed):
        if n == 1:
            return True
        elif n in existed:
            return False
        else:
            existed.append(n)

        n2 = 0
        while n > 0:
            n2 += (n % 10) ** 2
            n = n // 10
        return self.helper(n2,existed)

print(Solution().isHappy(2))
print((19 % 10) ** 2)