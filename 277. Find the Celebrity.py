# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def knows(a,b):
    if (a,b) == (0,1):
        return True
    else:
        return False

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return -1
        elif n == 1:
            return 0

        cand = [True for i in range(n)]
        for i in range(n):
            if cand[i] == True:
                for j in range(i + 1, n):
                    if cand[j] == True:
                        if knows(cand[i], cand[j]):
                            cand[i] = False
                        else:
                            cand[j] = False
        for i in range(n):
            if cand[i]:
                return i
                normals = [x for x in range(n) if x != i]
                for j in normals:
                    if knows(i, j) or not knows(j, i):
                        judge = False
                        break
                if judge: return i
        return -1

print(Solution().findCelebrity(6))