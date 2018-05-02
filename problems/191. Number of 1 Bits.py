class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")

    def hammingWeight2(self, n):

        ans = 0
        for i in range(32):
            ans += n & 1
            n >>= 1
        return ans

    def hammingWeight3(self, n):

        count = 0
        while n != 0:
            n = n & (n-1)
            count +=1
        return count



S1 = Solution().hammingWeight3(128)
print(S1)