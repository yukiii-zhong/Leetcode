class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapp = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in mapp:
                mapp[temp] = [s]
            else:
                mapp[temp].append(s)
        return list(mapp.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
