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

        for i in range(2, int((n - 1) ** 0.5) + 1):
            if notPrimes[i] == False:

                notPrimes[i*i:n:i] = len(notPrimes[i*i:n:i]) * [True]

        return notPrimes.count(False)



