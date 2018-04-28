class Solution:
    def countNumbersWithUniqueDigits(self, n):
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