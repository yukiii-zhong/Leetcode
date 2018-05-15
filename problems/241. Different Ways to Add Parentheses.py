class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # self.seen: Store the input and corresponding Computed answer list[]
        # Example: self.seen["2*3-4"] = [2,-2]
        self.seen = {}


        def oper(left,oper,right):
            """
            :param left: list[int]
            :param oper: str
            :param right: list[int]
            :return:
            """
            def helper(oper, a,b):

                if oper == "+":
                    return a + b
                elif oper == "-":
                    return a - b
                elif oper == "*":
                    return a * b

            return [helper(oper,a,b) for a in left for b in right]

        # If in put is ""
        if input is None: return []

        # If input is "23", return [23]
        if input.isalnum(): return [int(input)]

        if input in self.seen: return self.seen[input]

        # Normal Condition
        ans = []
        for i in range(len(input)):
            if not input[i].isalnum():
                ans += oper(self.diffWaysToCompute(input[:i]),input[i],self.diffWaysToCompute(input[i+1:]))

        self.seen[input] = ans
        return ans


test1 = Solution().diffWaysToCompute("2*3-4*5")
print(test1)
