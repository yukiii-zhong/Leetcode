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

        def isValid(s):
            if int(s) > 255:
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            return True

        res = []
        halves = findSplit(0, len(s), 2)
        for half in halves:
            lefts = findSplit(0, half, 1)
            rights = findSplit(half, len(s), 1)
            for l in lefts:
                for r in rights:
                    if all(isValid(string) for string in [s[:l], s[l:half], s[half:r], s[r:]]):
                        res.append(s[:l] + '.' + s[l:half] + '.' + s[half:r] + '.' + s[r:])

        return res