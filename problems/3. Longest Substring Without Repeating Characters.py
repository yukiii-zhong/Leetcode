class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        temp = []

        for ele in s:
            for i in range(len(temp)):
                if temp[i] == ele:
                    temp = temp[i + 1:]
                    break
            temp.append(ele)
            if len(temp) > longest:
                longest = len(temp)

        return longest