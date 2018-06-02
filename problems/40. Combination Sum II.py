class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(nums, start, tgt, temp):
            if tgt == 0:
                self.res.append(temp)
            else:
                for i in range(start, len(nums)):
                    if nums[i] > tgt: return
                    if i > start and nums[i] == nums[i - 1]: continue
                    dfs(nums, i + 1, tgt - nums[i], temp + [nums[i]])

        dfs(sorted(candidates), 0, target, [])
        return self.res