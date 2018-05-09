class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos = []
        key = []

        sList = list(s)
        for i in range(len(sList)):
            if sList[i] in 'aeiouAEIOU':
                pos.append(i)
                key.append(sList[i])

        for i in range(len(pos)):
            j = len(pos) -1 - i
            sList[pos[i]] = key[j]

        return "".join(sList)


    def reverseVowels2(self, s):
        vow = 'aeiouAEIOU'

        if len(s) <= 1: return s

        i = 0
        j = len(s)-1
        sList = list(s)

        while j>i:
            while j>i and sList[i] not in vow:
                i+=1
            while j>i and sList[j] not in vow:
                j-=1
            if i<j:
                sList[i],sList[j] = sList[j],sList[i]
                i +=1
                j -=1

        return "".join(sList)



print(Solution().reverseVowels2('hello'))