class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, i, j, ptr,seen):
            if ptr >= len(word):
                return True
            if (i,j) in seen: return False
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[ptr]:
                if dfs(board, word, i + 1, j, ptr + 1,seen+[(i,j)]) \
                        or dfs(board, word, i - 1, j, ptr + 1,seen+[(i,j)]) \
                        or dfs(board, word, i,j - 1,ptr + 1,seen+[(i,j)]) \
                        or dfs(board, word, i, j + 1, ptr + 1,seen+[(i,j)]):
                    return True
                else:
                    return False
            return False

        if len(word) == 0: return True
        if len(board) == 0 or len(board[0]) == 0: return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0,[]):
                    return True
        return False

    def exist2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, i, j, ptr):
            if ptr >= len(word):
                return True

            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[ptr]:
                temp = board[i][j]
                board[i][j] = '#'
                if dfs(board,word,i+1,j,ptr+1) or\
                        dfs(board,word,i-1,j,ptr+1)\
                        or dfs(board,word,i,j-1,ptr+1)\
                        or dfs(board,word,i,j+1,ptr+1):
                    return True
                board[i][j] = temp
            return False

        if len(board) == 0 or len(board[0]) == 0: return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        return False



print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))