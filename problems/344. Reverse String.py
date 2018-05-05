class Solution(object):
    # Time Limit Exceed
    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(len(s)-1,-1,-1):
            ans +=s[i]
        return ans

    def reverseString(self, s):

        n = len(s)
        if n == 0 or n == 1:
            return s

        mid = n//2
        return self.reverseString(s[mid:n]) + self.reverseString(s[0:mid])

    def reverseString3(self, s):
        return s[::-1]

    def reverseString4(self, s):
        i = 0
        j = len(s) -1

        sList = list(s)
        while i < j:
            sList[i],sList[j] = sList[j],sList[i]
            i+=1
            j-=1

        return "".join(sList)


print(Solution().reverseString4('hello'))



