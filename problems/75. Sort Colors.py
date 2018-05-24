class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # mapping: key = color num: nums[i], value = index
        mapping = {0: -1, 1: -1, 2: -1}

        i = 0
        while i < len(nums):
            if i == 0:
                mapping[nums[i]] = i
                i += 1
            elif nums[i - 1] < nums[i]:
                mapping[nums[i]] = i
                i += 1
            elif nums[i - 1] > nums[i]:
                if mapping[nums[i] + 1] != -1:
                    temp = mapping[nums[i] + 1]
                else:
                    temp = mapping[nums[i] + 2]
                nums[i], nums[temp] = nums[temp], nums[i]
                if mapping[nums[temp]] == -1:
                    mapping[nums[temp]] = temp
                mapping[nums[i]] = temp + 1
            else:
                i += 1



