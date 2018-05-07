class Solution:

    # Out of time limit
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(nums[0]+self.rob(nums[2:]), nums[1]+self.rob(nums[3:]))

    def rob2(self,nums):
        currmax = 0
        premax = 0

        for num in nums:
            temp = currmax
            currmax = max(premax + num, currmax)
            premax = temp

        return currmax



print(Solution().rob2([2,7,9,3,1]))