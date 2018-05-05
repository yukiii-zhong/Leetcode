class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        elif x == 0:
            return True

        # turn the int to an digit list
        dig = []
        while x > 0:
            dig.append(x % 10)
            x = x // 10

        def palinDig(dig):
            if len(dig) <=1:
                return True

            return dig[0] == dig[-1] and palinDig(dig[1:-1])

        return palinDig(dig)


    # In Python, you can directly tranfer the int to a String
    def isPalindrome2(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True

        str_x = str(x)

        i = 0
        j = len(str_x)-1

        while j>i:
            if str_x[i] == str_x[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    # Without extra space
    def isPalindrome3(self, x):

        if x <0 or (x % 10 ==0 and x != 0):
            return False

        reverted = 0

        while x > reverted:
            x, rem = x // 10, x % 10
            reverted = reverted *10 + rem

        return x == reverted or x == reverted // 10