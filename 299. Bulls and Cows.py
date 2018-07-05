class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        table = {}
        for dig in secret:
            if dig in table:
                table[dig] += 1
            else:
                table[dig] = 1
        A, B = 0, 0
        # count A
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
        # count A+B
        for dig in guess:
            if dig in table and table[dig] > 0:
                B += 1
                table[dig] -= 1
        B -= A
        return str(A)+'A'+str(B)+'B'

print(Solution().getHint('11111','01111'))