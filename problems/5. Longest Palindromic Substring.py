class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        m = 0
        while m < len(s):
            i = j = m
            while j < len(s) and s[i] == s[j]:
                j += 1
            j -= 1
            m = j

            while i - 1 > -1 and j + 1 < len(s) and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1

            if len(s[i:j + 1]) > len(longest):
                longest = s[i:j + 1]

            m += 1
        return longest


