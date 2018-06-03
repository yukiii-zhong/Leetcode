class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x = 0
        for i in range(len(nums)):
            if i <= 1 or nums[i] > nums[x - 2]:
                nums[x] = nums[i]
                x += 1

        return x

