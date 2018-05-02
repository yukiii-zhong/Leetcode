class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        diff = 0
        for num in nums:
            diff ^= num

        diff &= -diff
        res = [0,0]

        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res

test = Solution().singleNumber([1, 2, 1, 3, 2, 5])
print(test)