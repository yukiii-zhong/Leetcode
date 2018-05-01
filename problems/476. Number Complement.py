class Solution:
    # 建立一个"1111"，然后转换
    def findComplement2(self, num):
        """
        :type num: int
        :rtype: int
        """
        binum = bin(num)
        S = ""
        for i in range(len(binum) - 2):
            S += "1"
        i = int(S, 2)

        return i ^ num

    def findComplement(self, num):

        temp = 2 ** (len(bin(num))-2)-1

    def findComplement3(self, num):

        mask = ~0
        binlen = len(bin(num))-2
        for i in range(binlen):
            mask <<= 1

        return ~num ^ mask

ans = Solution().findComplement3(5)
