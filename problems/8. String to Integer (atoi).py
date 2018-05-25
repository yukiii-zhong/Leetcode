class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        mark = -1
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            else:
                if str[i].isnumeric():
                    mark = i
                if (str[i] == '+' or str[i] == '-') and i + 1 < len(str) and str[i + 1].isnumeric():
                    mark = i + 1
                break
        if mark == -1:
            return 0

        res = 0

        for i in range(mark, len(str)):
            if str[i].isnumeric():
                res = res * 10 + int(str[i])
                if res > 2 ** 31:
                    break
            else:
                break
        if mark - 1 >= 0 and str[mark - 1] == '-':
            res *= -1

        if res > (2 ** 31) - 1:
            res = (2 ** 31) - 1
        elif res < -(2 ** 31):
            res = - (2 ** 31)

        return res

print(Solution().myAtoi("    -42"))