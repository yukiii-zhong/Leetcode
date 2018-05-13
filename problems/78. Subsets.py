class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def helper(nums, temp):
            ans.append(temp)

            if len(nums) == 0: return

            for i in range(len(nums)):
                if i == len(nums) - 1:
                    helper([], temp + [nums[i]])
                else:
                    helper(nums[i + 1:], temp + [nums[i]])

        helper(nums, [])
        return ans
