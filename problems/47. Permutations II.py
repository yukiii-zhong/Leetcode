class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []

        def dfs(nums, temp):
            if len(temp) == n:
                res.append(temp)
                return

            for i in range(len(nums)):
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue
                else:
                    nums2 = nums[:]
                    nums2.remove(nums[i])
                    dfs(nums2, temp + [nums[i]])

        dfs(nums, [])
        return res


print(Solution().permuteUnique([1,1,2,2]))