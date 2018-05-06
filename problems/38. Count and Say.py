class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return '1'

        # When n>1
        # s --> last input
        s = self.countAndSay(n-1)

        # Use List
        res = []
        for i in range(len(s)):
            if i == 0:
                res += [1,s[i]]
            elif s[i] == s[i-1]:
                res[-2] += 1
            elif s[i] != s[i-1]:
                res += [1,s[i]]

        return "".join(str(i) for i in res)


        '''
        # Failed
        res = ''
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                res += str(count) + str(s[i-1])
                count = 1

        return res
        '''


print(Solution().countAndSay(6))