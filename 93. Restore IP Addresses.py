class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 2 or len(s) > 12: return []

        def findSplit(start, end, pairs):
            '''
            :rtype: List[int] A List sotre possible breaking points
            '''
            res = []
            for i in range(start + pairs * 1, start + pairs * 3 + 1):
                rem = end - i
                if pairs * 1 <= rem <= pairs * 3:
                    res.append(i)
            return res

        res = []
        halves = findSplit(0, len(s), 2)
        for half in halves:
            lefts = findSplit(0, half, 1)
            rights = findSplit(half, len(s), 1)
            for l in lefts:
                for r in rights:
                    if all(int(string) <= 255 for string in [s[:l], s[l:half], s[half:r], s[r:]]):
                        res.append(s[:l] + '.' + s[l:half] + '.' + s[half:r] + '.' + s[r:])

        return res

        def isValid(s):
            if

print(Solution().restoreIpAddresses("25525511135"))