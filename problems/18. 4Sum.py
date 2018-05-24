class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        nums.sort()
        res = []

        def getSum(start, N, target, temp):
            if nums[start] * N > target or nums[-1] * N < target:
                return
            if N == 2:
                l = start
                h = len(nums) - 1
                while h > l:
                    judge = nums[h] + nums[l]
                    if judge == target:
                        res.append(temp + [nums[l], nums[h]])
                        l += 1
                        h -= 1
                        while l < len(nums) and nums[l] == nums[l - 1]:
                            l += 1
                        while h >= 0 and nums[h] == nums[h + 1]:
                            h -= 1
                    elif judge < target:
                        l += 1
                    else:
                        h -= 1
                return

            for i in range(start, len(nums) - N + 1):
                if i == start or (i > start and nums[i - 1] != nums[i]):
                    getSum(i + 1, N - 1, target - nums[i], temp + [nums[i]])

        getSum(0, 4, target, [])
        return res
