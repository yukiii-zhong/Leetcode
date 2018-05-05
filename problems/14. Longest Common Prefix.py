class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        if len(strs) == 0:
            return res

        for i in range(len(strs[0])):
            if all(i < len(string) for string in strs) and all(strs[0][i] == string[i] for string in strs):
                res += strs[0][i]
            else:
                break
        return res