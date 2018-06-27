class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        nums.sort()
        ans = []

        def dfs(start, temp, nums):
            ans.append(temp)
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                else:
                    dfs(i + 1, temp + [nums[i]], nums)

        dfs(0, [], nums)
        return ans