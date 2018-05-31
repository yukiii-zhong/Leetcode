class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            nums = [0] * 10
            for j in range(9):
                if board[i][j] != '.':
                    a = int(board[i][j])
                    nums[a] += 1
                    if nums[a] > 1:
                        return False
        for j in range(9):
            nums = [0] * 10
            for i in range(9):
                if board[i][j] != '.':
                    a = int(board[i][j])
                    nums[a] += 1
                    if nums[a] > 1:
                        return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = [0] * 10
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        if board[a][b] != '.':
                            x = int(board[a][b])
                            nums[x] += 1
                            if nums[x] > 1:
                                return False

        return True


    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        clms = [set() for _ in range(9)]
        areas = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    a = board[i][j]
                    areaID = (i // 3) * 3 + j // 3
                    if a in rows[i] or a in clms[j] or a in areas[areaID]:
                        return False
                    else:
                        rows[i].add(a)
                        clms[j].add(a)
                        areas[areaID].add(a)
        return True