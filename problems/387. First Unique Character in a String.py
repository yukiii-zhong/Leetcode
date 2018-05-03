class Solution(object):

    # Too slow, abandon it
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return -1

        if s[0] not in s[1:]:
            return 0
        for i in range(1, n - 1):
            if s[i] not in s[0:i] and s[i] not in s[i + 1: n]:
                return i
        if s[n - 1] not in s[:-1]:
            return n - 1
        return -1

    def firstUniqChar2(self, s):

        dic = {}
        for char in set(s):
            dic[char] = s.count(char)
        for i,char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1




print(Solution().firstUniqChar("leetcode"))