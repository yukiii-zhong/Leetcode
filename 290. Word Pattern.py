class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split(' ')
        if not strList or len(strList) != len(pattern): return False
        table = {}
        for i in range(len(pattern)):
            if pattern[i] not in table:
                if strList[i] in table.values(): return False
                table[pattern[i]] = strList[i]
            # pattern[i] in table
            elif strList[i] != table[pattern[i]]:
                return False
        return True

print(Solution().wordPattern(pattern = "abba", str = "dog cat cat fish"))