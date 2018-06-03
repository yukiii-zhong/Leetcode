class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False

        m = len(matrix)
        n = len(matrix[0])

        def searchLine(A, st, ed, tgt):
            if st == ed:
                if A[st][0] <= tgt <= A[st][-1]:
                    return st
                else:
                    return -1
            elif st > ed:
                return -1

            # st < ed
            mid = (st + ed) // 2
            if A[mid][0] <= tgt <= A[mid][-1]:
                return mid
            elif tgt < A[mid][0]:
                return searchLine(A, st, mid - 1, tgt)
            else:
                return searchLine(A, mid + 1, ed, tgt)

        line = searchLine(matrix, 0, m - 1, target)

        if line == -1:
            return False

        def searchclm(line, st, ed, tgt):
            if st == ed:
                if line[st] == tgt:
                    return st
                else:
                    return -1
            elif st > ed:
                return -1

            mid = (st + ed) // 2
            if line[mid] == tgt:
                return mid
            elif line[mid] < tgt:
                return searchclm(line, mid + 1, ed, tgt)
            else:
                return searchclm(line, st, mid - 1, tgt)

        clm = searchclm(matrix[line], 0, len(matrix[line]) - 1, target)
        if clm == -1:
            return False
        else:
            return True