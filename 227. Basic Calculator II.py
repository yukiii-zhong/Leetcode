class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        def isOp(s):
            if s in ['+', '-', '*', '/']:
                return True
            else:
                return False

        def Op(num1, num2, op):
            if num1==0 or num2 == 0: return 0
            flag = -1 if num1*num2<0 else 1
            if op == '*':
                return num1 * num2
            elif op == '/':
                return abs(num1) // abs(num2) * flag

        i = j = 0
        lastOp = ''
        nums = []
        while i < len(s) and j <= len(s):
            if s[i] == ' ':
                i += 1
                j += 1
            elif j == len(s) or isOp(s[j]):
                num = int(s[i:j])
                if lastOp in ['*', '/']:
                    temp = Op(nums.pop(), num, lastOp)
                    nums.append(temp)
                elif lastOp == '-':
                    nums.append(num * -1)
                else:
                    nums.append(num)
                if j < len(s):
                    lastOp = s[j]
                i = j = j + 1
            else:
                j += 1

        return nums

print(Solution().calculate("14-3/2"))
print(3 //2)