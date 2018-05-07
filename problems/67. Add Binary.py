class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    # Recursion: 
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


    # 用指针，计算每一位的sum, return
    def addBinary3(self, a, b):
        i = len(a)-1
        j = len(b)-1
        ans = ""
        carry = 0

        # 此处，我只需要a[i] +b[j] + carry的sum，只要其中有一个存在，就继续，
        # 确定一个存在，就再加一个
        while j>=0 or i>=0 or carry>0:
            temp = carry
            if i>= 0:
                temp += int(a[i])
                i-=1
            if j>=0:
                temp += int(b[j])
                j-=1

            carry = temp //2
            ans = str(temp % 2) + ans

        return ans




print(Solution().addBinary3('1010','1011'))