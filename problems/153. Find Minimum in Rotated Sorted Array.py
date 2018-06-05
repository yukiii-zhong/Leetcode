class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def dfs(nums, s, e):
            if nums[s] <= nums[e]:
                return nums[s]
            else:
                # nums[s]>nums[e]
                m = (s + e) // 2
                if nums[s] < nums[m]:
                    return dfs(nums, m + 1, e)
                elif nums[s] == nums[m]:
                    nums[e]
                else:
                    return min(dfs(nums, s, m - 1), dfs(nums, m, e))

        return dfs(nums, 0, len(nums) - 1)

