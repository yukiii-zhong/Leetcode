class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]

        vals = list(mapping.values())
        vals.sort()

        for i in range(len(vals)-1):
            if vals[i] == vals[i+1]:
                return False

        return True

print(Solution().isIsomorphic("a","a"))