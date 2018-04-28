class Solution:

    # Method1 exceeds time limit
    def countNumbersWithUniqueDigits2(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.res = 10 ** n

        def helper(n, set):

            if n <= 0:
                return

            if len(set) == 0:
                helper(n-1 , set)

                for i in range(1,10):
                    helper(n-1,set+[i])
            else:
                for i in range(10):
                    if i in set:
                        self.res -= 10 ** (n-1)
                    else:
                        helper(n-1,set +[i])

        helper(n,[])
        return self.res

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 1

        if n == 0:
            return count

        if n > 10:
            return self.countNumbersWithUniqueDigits(10)

        k = 9
        for i in range(n):
            count *=k
            if i !=0:
                k -=1

        count += self.countNumbersWithUniqueDigits(n-1)
        return count