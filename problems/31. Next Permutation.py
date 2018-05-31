class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]

                        x = i + 1
                        y = len(nums) - 1
                        while x < y:
                            nums[x], nums[y] = nums[y], nums[x]
                            x += 1
                            y -= 1

                        return

        nums.sort()