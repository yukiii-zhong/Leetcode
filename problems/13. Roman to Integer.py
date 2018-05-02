class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic1 = {'I':1, 'V':5, 'X':10,
                'L':50, 'C':100, 'D':500,
                'M':1000}
        dic2 = {'IV':-2,'IX':-2,
                'XL':-20, 'XC':-20,
                'CD':-200, 'CM':-200}
        ans = 0

        for i in range(len(s)-1):
            ans += dic1[s[i]]
            if s[i:i+2] in dic2:
                ans += dic2[s[i:i+2]]
        ans += dic1[s[-1]]

        return ans

    def romanToInt2(self, s):
        dic = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500,
                'M': 1000}

        ans = 0

        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]] :
                ans -= dic[s[i]]
            else:
                ans +=dic[s[i]]

        ans += dic[s[-1]]

        return ans



test1 = Solution().romanToInt2('MCMXCIV')
print(test1)
