class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = [[]]

        for char in S:
            n = len(ans)

            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)


        ans2 = []
        for i in range(len(ans)):
            ans2.append("".join(ans[i]))

        return ans2

    def letterCasePermutation2(self, S):

        ans = [""]

        for char in S:
            if char.isalpha():
                for i in range(len(ans)):
                    ans.append(ans[i]+char.upper())
                    ans[i] += char.lower()
            else:
                for i in range(len(ans)):
                    ans[i] +=char
        return ans

