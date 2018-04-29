class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0

        for i in nums:
            a ^= i

        return a