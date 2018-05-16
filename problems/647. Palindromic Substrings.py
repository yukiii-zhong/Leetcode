class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        isPali = [[False] * len(s)] * len(s)

        for i in range(len(s)):
            isPali[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                isPali[i][i + 1] = True

        for i in range(1, len(s) - 1):
            for j in range(i, len(s) - 1):
                if isPali[i][j]:
                    isPali[i - 1][j + 1] = (s[i - 1] == s[j + 1])

        count = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if isPali[i][j]:
                    count += 1
        return count

print(Solution().countSubstrings("cca"))