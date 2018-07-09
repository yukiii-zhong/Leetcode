class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left, right = max(E,A), min(C,G)
        top, bottom = min(D,H), max(B,F)
        if left >= right or bottom>= top:
            left = right

        return (C-A)*(D-B) + (G-E)*(H-F) - (right-left)*(top-bottom)