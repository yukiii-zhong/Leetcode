class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        mem = [-1] * (len(s) + 1)
        mem[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                mem[i] = 0
            elif i == len(s) - 1:
                mem[i] = 1
            else:
                # s[i] != '0' and i<len(s)-1
                mem[i] = mem[i + 1]
                if int(s[i]) * 10 + int(s[i + 1]) <= 26:
                    mem[i] += mem[i + 2]

        return mem[0]