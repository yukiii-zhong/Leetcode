class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        mem = {}
        words = {w for w in wordDict}

        def dfs(s):
            if s in mem:
                return mem[s]

            for i in range(0, len(s)):
                mem[s[0:i]] = dfs(s[0:i])
                if mem[s[0:i]] and s[i:len(s)] in words:
                    return True
            return False

        return dfs(s)
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Return a set
        words = {w for w in wordDict}
        # set is faster than List
        OK = [False] * (len(s)+1)
        OK[0] = True
        for i in range(len(s)+1):
            for j in range(i+1):
                if OK[j] and s[j:i] in words:
                    OK[i] = True
                    break
        return OK[-1]


print(Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"]
))