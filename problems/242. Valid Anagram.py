class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}

        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        for char in t:
            if char not in dic:
                return False
            else:
                dic[char] -=1
                if dic[char] == 0: del(dic[char])

        return dic == {}


    # turn the string into the list
    # Sorting the list
    # Compare the sorted list
    def isAnagram2(self,s,t):

        L_s = list(s)
        L_t = list(t)
        L_s.sort()
        L_t.sort()
        return L_s == L_t

print(Solution().isAnagram2('b','ab'))

