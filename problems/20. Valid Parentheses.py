class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dic = {'(':-1, '[':-2, '{':-3, ')':1, ']':2, '}':3}

        temp = []

        for para in s:

            if dic[para] < 0:
                temp.append(para)
            elif dic[para] > 0 and len(temp) and dic[temp[-1]] + dic[para] == 0:
                temp.pop()
            else:
                return False

        if len(temp) == 0:
            return True
        else:
            return False

test1 = ')'
test2 = '[(){}]'
test3 = '[(])'
print(Solution().isValid(test1))