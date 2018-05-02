class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        for i in range(num+1):
            ans.append(bin(i).count("1"))
        return ans


    # P(x) = P(x & (x-1)) + 1
    def countBits2(self, num):

        ans = [0]
        if num == 0: return ans

        for i in range(1,num+1):
            ans.append(ans[i & (i-1)] +1)

        return ans

test1 = Solution().countBits2(0)
print(test1)