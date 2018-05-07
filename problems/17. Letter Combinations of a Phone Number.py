class Solution:
    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmap = {'2':['a','b','c'], '3':['d','e','f'],'4': ['g','h','i'], '5': ['j','k','l'],
               '6': ['m','n','o'], '7': ['p','q','r','s'],'8': ['t','u','v'],'9':['w','y','z']}

        res = []

    def letterCombinations(self, digits):
        mapping = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []

        if len(digits) == 0:
            return res
        elif len(digits) == 1:
            return list(mapping[int(digits)])

        pre = self.letterCombinations(digits[:-1])
        additional = mapping[int(digits[-1])]
        return [s+c for s in pre for c in additional]


print(Solution().letterCombinations('234'))