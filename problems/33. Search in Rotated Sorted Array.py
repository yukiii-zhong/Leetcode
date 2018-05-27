class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1

        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if target == nums[mid]:
                return mid

            elif nums[mid] <= nums[j]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif nums[mid] >= nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1

        return -1

print(Solution().search([],3))