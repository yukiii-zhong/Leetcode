class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0

        notPrimes = [False] * n
        notPrimes[0] = True
        notPrimes[1] = True

        for i in range(2, n - 1):
            if notPrimes[i] == False:
                for k in range(2 * i, n, i):
                    notPrimes[k] = True

        return notPrimes.count(False)



