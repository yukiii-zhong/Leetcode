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

print(Solution().reverseVowels('leetcode'))