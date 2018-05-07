class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0

        n = len(needle)
        for i in range(len(haystack)-(n-1)):
            if haystack[i:i+n] == needle:
                return i

        return -1

print(Solution().strStr("hello","ll"))
