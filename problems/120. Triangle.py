class Solution(object):
    def minimumTotal(self, tri):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(tri) == 0:
            return 0

        for i in range(len(tri) - 2, -1, -1):
            # in tri[i]
            for j in range(len(tri[i])):
                tri[i][j] += min(tri[i + 1][j], tri[i + 1][j + 1])

        return tri[0][0]