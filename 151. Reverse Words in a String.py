class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wList = []
        i = j = 0

        while True:
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s): break
            # s[j] not included
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            wList.append(s[i:j])
            i = j

        wList.reverse()
        return " ".join(wList)

print(Solution().reverseWords("   the   sky is   blue   "))