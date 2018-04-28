class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []

        def helper(S,n,left,right):

            if right == n:
                self.ans.append(S)
                return

            if right < left:
                helper(S+")",n,left,right+1)

            if left < n:
                helper(S + "(",n,left+1,right)

        helper("",n,0,0)

        return self.ans