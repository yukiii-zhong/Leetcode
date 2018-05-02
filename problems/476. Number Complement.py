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
        n = len(bin(num)) - 2
        temp = 2 ** n - 1
        return num ^ temp

    def findComplement3(self, num):

        mask = ~0
        for i in range(len(bin(num))-2):
            mask <<= 1

        return ~num ^ mask

ans = Solution().findComplement3(5)
print(ans)
