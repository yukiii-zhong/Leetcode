class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        if len(strs) == 0:
            return res

        sentinel = min(strs, key=len)

        for i in range(len(sentinel)):
            if all(sentinel[i] == string[i] for string in strs):
                res += sentinel[i]
            else:
                break
        return res

