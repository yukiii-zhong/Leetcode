class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a

        temp = int(a[-1]) + int(b[-1])

        if temp <2:
            return self.addBinary(a[:-1],b[:-1]) + str(temp)
        elif temp >= 2:
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1') + str(temp-2)

print(Solution().addBinary2('1010','1011'))