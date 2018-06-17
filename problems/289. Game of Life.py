class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def liveNBs(board, i, j):
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x == i and y == j) or x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                        continue
                    elif board[x][y] % 10 == 1:
                        count += 1
            return count
        # test
        return liveNBs(board, 2, 1)

        if not board: return

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] += 10 * liveNBs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                a = board[i][j] // 10
                b = board[i][j] % 10

                if b == 0:
                    if a == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                elif b == 1:
                    if a < 2 or a > 3:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1


