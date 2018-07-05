class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0

        n = len(citations)
        counts = [0 for i in range(n + 1)]

        for cit in citations:
            if cit >= n:
                counts[n] += 1
            else:
                counts[cit] += 1

        for i in range(n, -1, -1):
            if counts[i] >= i:
                return i
            elif i - 1 >= 0:
                counts[i - 1] += counts[i]

        return 0