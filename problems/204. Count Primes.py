class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 0

        notPrimes = [False] * n
        notPrimes[0] = True
        notPrimes[1] = True

        for i in range(2, n - 1):
            if notPrimes[i] == False:
                k = i + i
                while k <= (n - 1):
                    notPrimes[k] = True
                    k += i

        return notPrimes.count(False)



