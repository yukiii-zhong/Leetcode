class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.mem = [-1] * (len(s) + 1)

        def dfs(i):
            if self.mem[i] != -1:
                return self.mem[i]

            if i == len(s):
                return 1
            # Then i < len(s)
            elif s[i] == '0':
                return 0
            # Then i<len(s), and s[i] != '0'
            elif i == len(s) - 1:
                return 1

            # i<len(s)-1, s[i] != '0'
            self.mem[i] = 0
            if int(s[i:i + 2]) <= 26:
                self.mem[i] += dfs(i + 2)
            self.mem[i] += dfs(i + 1)

            return self.mem[i]

        return dfs(0)
