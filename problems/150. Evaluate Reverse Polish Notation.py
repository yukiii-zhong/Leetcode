class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        if len(tokens) == 1: return int(tokens[0])

        def oper(s1, s2, op):
            a, b = int(s1), int(s2)
            if op == '-':
                return a - b
            elif op == '+':
                return a + b
            elif op == '*':
                return a * b
            elif op == '/':
                return int(a / b)

        stack = []
        for s in tokens:
            if s not in {'-', '+', '*', '/'}:
                stack.append(s)
            else:
                temp = oper(stack[-2], stack[-1], s)
                stack.pop()
                stack.pop()
                stack.append(str(temp))
        return int(stack[0])