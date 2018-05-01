class Solution:
    # 该用法适用于JAVA，Python负数使用有问题
    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a

        temp = a ^b
        carry = (a &b )<< 1

        return self.getSum(temp, carry)

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF

        while b !=0:
            a, b = (a^b) & mask, ((a&b)<<1) & mask

        return a if a <= MAX else ~(a ^ mask)

test1 = Solution().getSum(2,-3)
print(test1)