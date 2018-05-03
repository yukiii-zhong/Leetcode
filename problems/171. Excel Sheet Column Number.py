class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            ans += (ord(s[i])-64) * (26 **(len(s)-i-1))

        return ans

    # Faster one
    def titleToNumber2(self, s):
        ans = 0
        for char in s:
            ans = ans * 26 + ord(char) - 64

        return ans


print(Solution().titleToNumber2('ZY'))