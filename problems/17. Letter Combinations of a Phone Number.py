class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmap = {'2':['a','b','c'], '3':['d','e','f'],'4': ['g','h','i'], '5': ['j','k','l'],
               '6': ['m','n','o'], '7': ['p','q','r','s'],'8': ['t','u','v'],'9':['w','y','z']}

        res = []



print(Solution().letterCombinations('23'))